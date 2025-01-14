import paho.mqtt.client as mqtt
import json
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from celery import shared_task
from eyefleet.apps.livetracking.models import Device, Indicator
from influxdb_client import InfluxDBClient, Point, BucketRetentionRules
from influxdb_client.client.write_api import SYNCHRONOUS
from django.conf import settings


# define influxdb configurations
INFLUXDB_CONFIG = {
    'url': settings.INFLUXDB_URL,
    'token': settings.INFLUXDB_TOKEN,
    'org': settings.INFLUXDB_ORG
}

# Initialize InfluxDB client
client = InfluxDBClient(**INFLUXDB_CONFIG)
write_api = client.write_api(write_options=SYNCHRONOUS)
buckets_api = client.buckets_api()

# Retention policy configuration
RETENTION_DAYS = 30
RETENTION_SECONDS = RETENTION_DAYS * 86400

@shared_task
def mqtt_receiver():
    """
    Continuous task that subscribes to MQTT broker and processes incoming messages
    """
    def on_connect(client, userdata, flags, rc):
        print(f"Connected to MQTT broker with result code {rc}")
        client.subscribe(settings.MQTT_TOPIC)

    def on_message(client, userdata, msg):
        try:
            data = json.loads(msg.payload.decode())
            process_message(data)
        except json.JSONDecodeError as e:
            print(f"Failed to decode MQTT message: {e}")
        except Exception as e:
            print(f"Error processing MQTT message: {e}")

    def process_message(data):
        # Get or create device
        try:
            device = Device.objects.get(id=data["device"])
        except Device.DoesNotExist:
            print(f"received message from unknown device : {data['device']}")
            return
        
        print(f"received message from device: {device.id}")
        try:
            data_timestamp = data["timestamp"]
            device_data: dict = data["data"]
        except KeyError as e:
            print(f"missing required fields in mqtt message: {e}")
            return

        # Process device data and store in InfluxDB
        for key, value in device_data.items():
            # Get or create indicator
            try:
                indicator: Indicator = Indicator.objects.get(name=key)
            except Indicator.DoesNotExist:
                print(f"indicator not found: {key}")
                print(f"creating indicator: {key}")
                indicator = Indicator.objects.create(name=key, computed=False)
                print(f"indicator created: {indicator.id}")
            except Indicator.MultipleObjectsReturned:
                print(f"multiple indicators found: {key}")
                indicator = Indicator.objects.filter(name=key).first()
                return

            # store data in influxdb bucket
            try:
                # format bucket name
                bucket_name = device.id.replace(" ", "").lower()
                
                # create or get bucket with retention policy
                bucket = buckets_api.find_bucket_by_name(bucket_name)
                if not bucket:
                    bucket = buckets_api.create_bucket(
                        bucket_name=bucket_name,
                        retention_rules=[
                            BucketRetentionRules(
                                type="expire",
                                every_seconds=RETENTION_SECONDS
                            )
                        ]
                    )

                # Create and write data point
                point = Point(indicator.name) \
                    .tag("unit", indicator.unit) \
                    .field("value", value) \
                    .time(data_timestamp)

                write_api.write(
                    bucket=bucket_name,
                    org=INFLUXDB_CONFIG['org'],
                    record=point
                )
                print(f"data point written to influxdb: {point}")

            except Exception as e:
                print(f"failed to save data point to influxdb: {e}")
                continue

        # Broadcast OBD data via websockets
        try:
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                f"obd_{device.id}",
                {
                    "type": "live_vehicle_data_message",
                    "message": device_data
                }
            )
            print(f"successfully sent obd data message via websocket")
        except Exception as e:
            print(f"failed to broadcast obd data via websocket: {e}")

        # Broadcast GPS data via websockets
        try:
            async_to_sync(channel_layer.group_send)(
                "gps_group",
                {
                    "type": "send_gps_data",
                    "message": {
                        "device": str(device.id),
                        "asset": str(device.assigned_asset.id),
                        "longitude": device_data["longitude"],
                        "latitude": device_data["latitude"],
                        "timestamp": data["timestamp"],
                        "speed": device_data["speed"]
                    }
                }
            )
            print(f"successfully sent gps data message via websocket")
        except Exception as e:
            print(f"failed to broadcast gps data via websocket: {e}")

    # Set up MQTT client
    mqtt_client = mqtt.Client()
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message

    # Connect to MQTT broker
    mqtt_client.connect(settings.MQTT_BROKER_HOST, settings.MQTT_BROKER_PORT, 60)

    # Start the loop forever
    mqtt_client.loop_forever()