from django.core.management.base import BaseCommand
from eyefleet.apps.livetracking.tasks.mqtt_simulator import generate_device_telemetry

class Command(BaseCommand):
    help = 'Starts the MQTT simulator to generate device telemetry'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting MQTT simulator...'))
        try:
            generate_device_telemetry()
        except KeyboardInterrupt:
            self.stdout.write(self.style.SUCCESS('MQTT simulator stopped'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))