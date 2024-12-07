# Generated by Django 4.2.16 on 2024-11-26 10:32

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('weight', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('volume', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('description', models.TextField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('pickup_point', models.CharField(blank=True, max_length=255, null=True)),
                ('dropoff_point', models.CharField(blank=True, max_length=255, null=True)),
                ('expected_pickup_t', models.DateTimeField(blank=True, null=True)),
                ('expected_dropoff_t', models.DateTimeField(blank=True, null=True)),
                ('has_return', models.BooleanField(default=False)),
                ('special_instructions', models.JSONField(blank=True, null=True)),
                ('sender', models.CharField(blank=True, max_length=100, null=True)),
                ('receiver', models.CharField(blank=True, max_length=100, null=True)),
                ('handler', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'cargo',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='CargoPriority',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'cargo_priorities',
            },
        ),
        migrations.CreateModel(
            name='CargoStatus',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'cargo_statuses',
            },
        ),
        migrations.CreateModel(
            name='CargoType',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'cargo_types',
            },
        ),
        migrations.CreateModel(
            name='ClientContactMethod',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'client_contact_methods',
            },
        ),
        migrations.CreateModel(
            name='ClientPriority',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'client_priorities',
            },
        ),
        migrations.CreateModel(
            name='ClientService',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'client_services',
            },
        ),
        migrations.CreateModel(
            name='ClientSource',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'client_sources',
            },
        ),
        migrations.CreateModel(
            name='ClientStatus',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'client_statuses',
            },
        ),
        migrations.CreateModel(
            name='ClientType',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'client_types',
            },
        ),
        migrations.CreateModel(
            name='DriverStatus',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'driver_statuses',
            },
        ),
        migrations.CreateModel(
            name='PaymentStatus',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'payment_statuses',
            },
        ),
        migrations.CreateModel(
            name='ReportFormat',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'report_formats',
            },
        ),
        migrations.CreateModel(
            name='ReportFrequency',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'report_frequencies',
            },
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('route_number', models.CharField(max_length=20, unique=True)),
                ('driver', models.CharField(blank=True, max_length=20, null=True)),
                ('vehicle', models.CharField(blank=True, max_length=100, null=True)),
                ('stops', models.PositiveIntegerField(default=0)),
                ('description', models.TextField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('total_weight', models.FloatField(blank=True, null=True)),
                ('total_volume', models.FloatField(blank=True, null=True)),
                ('stop_points', models.JSONField(default=list)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cargos', models.ManyToManyField(to='routes.cargo')),
            ],
            options={
                'db_table': 'routes',
            },
        ),
        migrations.CreateModel(
            name='RouteAlertPriority',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'alert_priorities',
            },
        ),
        migrations.CreateModel(
            name='RouteAlertStatus',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'alert_statuses',
            },
        ),
        migrations.CreateModel(
            name='RouteAlertType',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'alert_types',
            },
        ),
        migrations.CreateModel(
            name='RouteAssignedEmployeeRole',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'route_assigned_employee_roles',
            },
        ),
        migrations.CreateModel(
            name='RoutePriority',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'route_priorities',
            },
        ),
        migrations.CreateModel(
            name='RouteReportStatus',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'report_statuses',
            },
        ),
        migrations.CreateModel(
            name='RouteReportType',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('queries', models.JSONField(blank=True, default=list, null=True)),
                ('template', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'report_types',
            },
        ),
        migrations.CreateModel(
            name='RouteScheduleRecurrence',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'schedule_recurrences',
            },
        ),
        migrations.CreateModel(
            name='RouteScheduleShift',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'schedule_shifts',
            },
        ),
        migrations.CreateModel(
            name='RouteScheduleStatus',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'route_schedule_statuses',
            },
        ),
        migrations.CreateModel(
            name='RouteStatus',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'route_statuses',
            },
        ),
        migrations.CreateModel(
            name='TripStatus',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'trip_statuses',
            },
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('reference_route', models.CharField(blank=True, max_length=50, null=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('source', models.CharField(max_length=255)),
                ('destination', models.CharField(max_length=255)),
                ('driver', models.CharField(max_length=100)),
                ('staff', models.JSONField(default=list)),
                ('passengers', models.JSONField(default=list)),
                ('on_time', models.BooleanField(default=True)),
                ('progress', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('status', models.ForeignKey(default='ongoing', on_delete=django.db.models.deletion.PROTECT, to='routes.tripstatus')),
                ('vehicle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='vehicles.vehicle')),
            ],
            options={
                'db_table': 'route_logs',
            },
        ),
        migrations.CreateModel(
            name='RouteSchedule',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('schedule_id', models.CharField(max_length=20, unique=True)),
                ('driver', models.CharField(blank=True, max_length=20, null=True)),
                ('vehicle', models.CharField(blank=True, max_length=100, null=True)),
                ('route', models.CharField(max_length=255)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('deliveries', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('estimated_duration', models.CharField(max_length=50)),
                ('notes', models.TextField(blank=True, null=True)),
                ('actual_duration', models.CharField(blank=True, max_length=50, null=True)),
                ('total_stops', models.PositiveIntegerField(default=0)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
                ('assigned_by', models.CharField(blank=True, max_length=100, null=True)),
                ('next_occurrence', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('recurrence', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='routes.routeschedulerecurrence')),
                ('shift', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='routes.routescheduleshift')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='routes.routeschedulestatus')),
            ],
        ),
        migrations.CreateModel(
            name='RouteReport',
            fields=[
                ('id', models.CharField(default='ROUTEREP-', max_length=20, primary_key=True, serialize=False)),
                ('report_name', models.CharField(max_length=255)),
                ('generated_at', models.DateTimeField()),
                ('date_range_start', models.DateField()),
                ('date_range_end', models.DateField()),
                ('file_size', models.CharField(max_length=20)),
                ('last_accessed', models.DateTimeField()),
                ('generated_by', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('tags', models.JSONField(default=list)),
                ('recipients', models.JSONField(default=list)),
                ('is_archived', models.BooleanField(default=False)),
                ('comments', models.JSONField(default=list)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('format', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='routes.reportformat')),
                ('frequency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='routes.reportfrequency')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='routes.route')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='routes.routereportstatus')),
            ],
            options={
                'db_table': 'reports',
                'ordering': ['-generated_at'],
            },
        ),
        migrations.CreateModel(
            name='RouteAssignedEmployee',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('employee', models.CharField(max_length=100)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='routes.routeassignedemployeerole')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='routes.route')),
            ],
        ),
        migrations.CreateModel(
            name='RouteAlert',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('route', models.CharField(blank=True, max_length=50, null=True)),
                ('driver', models.CharField(blank=True, max_length=50, null=True)),
                ('location', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('impact', models.TextField()),
                ('estimated_delay', models.CharField(blank=True, max_length=50, null=True)),
                ('assigned_to', models.CharField(blank=True, max_length=50, null=True)),
                ('resolution', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('resolved_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('priority', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='routes.routealertpriority')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='routes.routealertstatus')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='routes.routealerttype')),
            ],
            options={
                'db_table': 'route_alerts',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.AddField(
            model_name='route',
            name='priority',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='routes.routepriority'),
        ),
        migrations.AddField(
            model_name='route',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='routes.routestatus'),
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('employee_reference', models.CharField(blank=True, max_length=20, null=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('license_number', models.CharField(blank=True, max_length=50, null=True)),
                ('license_expiry', models.DateTimeField(blank=True, null=True)),
                ('total_trips', models.PositiveIntegerField(default=0)),
                ('total_distance', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('rating', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('organization', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.ForeignKey(default='active', on_delete=django.db.models.deletion.PROTECT, to='routes.driverstatus')),
            ],
            options={
                'db_table': 'drivers',
                'ordering': ['first_name', 'last_name'],
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('contact_phone', models.CharField(max_length=20)),
                ('contact_email', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator()])),
                ('location', models.JSONField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('avatar', models.URLField()),
                ('case_ref', models.CharField(max_length=50, unique=True)),
                ('opened_at', models.DateField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('assigned_agent', models.CharField(blank=True, max_length=100, null=True)),
                ('next_follow_up', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='routes.client')),
                ('payment_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='routes.paymentstatus')),
                ('preferred_contact_method', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='routes.clientcontactmethod')),
                ('priority', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='routes.clientpriority')),
                ('services', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='routes.clientservice')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='routes.clientsource')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='routes.clientstatus')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='routes.clienttype')),
            ],
            options={
                'db_table': 'clients',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='cargo',
            name='priority',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='routes.cargopriority'),
        ),
        migrations.AddField(
            model_name='cargo',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='routes.cargostatus'),
        ),
        migrations.AddField(
            model_name='cargo',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='routes.cargotype'),
        ),
        migrations.AddIndex(
            model_name='route',
            index=models.Index(fields=['route_number'], name='routes_route_n_320591_idx'),
        ),
    ]