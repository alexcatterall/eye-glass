import factory
from factory.django import DjangoModelFactory
from factory import fuzzy
import random
from django.utils import timezone
from datetime import timedelta

from telemex.apps.vehicles.models import Vehicle, VehicleStatus, VehicleType


class VehicleFactory(DjangoModelFactory):
    class Meta:
        model = Vehicle

    registration_number = factory.Sequence(lambda n: f'ABC{n:03d}')
    manufacturer = factory.Faker('company')
    model = factory.Faker('word')

    type = factory.Iterator(VehicleType.objects.all())

    driver = factory.Faker('name')
    status = factory.Iterator(VehicleStatus.objects.all())
    location = factory.LazyFunction(
        lambda: {
            'latitude': float(fuzzy.FuzzyDecimal(-90, 90, precision=6).fuzz()),
            'longitude': float(fuzzy.FuzzyDecimal(-180, 180, precision=6).fuzz())
        }
    )
    fuel_level = fuzzy.FuzzyInteger(0, 100)
    on_trip = factory.LazyAttribute(
        lambda o: True if o.status.id == 'on route' else random.choice([True, False])
    )
    mileage = factory.LazyFunction(
        lambda: f"{random.randint(1000, 500000)} km"
    )
    created_at = factory.LazyFunction(
        lambda: timezone.now() - timedelta(days=random.randint(0, 365))
    )
    updated_at = factory.LazyAttribute(
        lambda o: o.created_at + timedelta(days=random.randint(0, 30))
    )