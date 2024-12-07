# Generated by Django 5.1.4 on 2024-12-07 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('license_plate', models.CharField(max_length=20)),
                ('vin', models.CharField(max_length=17)),
                ('mileage', models.IntegerField()),
                ('fuel_type', models.CharField(choices=[('gasoline', 'Gasoline'), ('diesel', 'Diesel'), ('electric', 'Electric'), ('hybrid', 'Hybrid')], max_length=20)),
                ('status', models.CharField(choices=[('active', 'Active'), ('maintenance', 'In Maintenance'), ('retired', 'Retired')], max_length=20)),
                ('location_lat', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('location_lng', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
