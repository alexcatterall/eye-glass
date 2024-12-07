# Generated by Django 4.2.17 on 2024-12-07 13:55

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceConfiguration',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('device_type', models.CharField(choices=[('eyefleet-hardware', 'eyefleet Hardware'), ('autopi', 'AutoPi')], max_length=50)),
                ('firmware_version', models.CharField(max_length=20)),
                ('settings', models.JSONField(default=dict)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'device_configurations',
            },
        ),
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('id', models.CharField(default='IND-', max_length=20, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('computed', models.BooleanField(default=False)),
                ('compute_func', models.CharField(blank=True, help_text='Function to compute indicator', max_length=255, null=True)),
                ('data_type', models.CharField(blank=True, choices=[('integer', 'Integer'), ('float', 'Float'), ('boolean', 'Boolean'), ('string', 'String')], max_length=50, null=True)),
                ('unit', models.CharField(default='unk', help_text='unit of measurement', max_length=50)),
                ('CAN_bus_code', models.CharField(blank=True, help_text='CAN bus code to read indicator', max_length=50, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('min_value', models.FloatField(blank=True, null=True)),
                ('max_value', models.FloatField(blank=True, null=True)),
                ('warning_threshold', models.FloatField(blank=True, null=True)),
                ('critical_threshold', models.FloatField(blank=True, null=True)),
                ('enabled', models.BooleanField(default=True)),
                ('last_reading', models.FloatField(blank=True, null=True)),
                ('last_reading_time', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'indicators',
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.CharField(default='DEV-', max_length=20, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('ip_address', models.GenericIPAddressField()),
                ('connected', models.BooleanField(default=False)),
                ('last_pinged', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('status', models.CharField(blank=True, choices=[('online', 'Online'), ('offline', 'Offline'), ('maintenance', 'Maintenance'), ('error', 'Error')], default='offline', max_length=50, null=True)),
                ('location', models.JSONField(blank=True, null=True)),
                ('battery_level', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('assigned_vehicle', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('configuration', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='livetracking.deviceconfiguration')),
            ],
            options={
                'db_table': 'devices',
            },
        ),
    ]
