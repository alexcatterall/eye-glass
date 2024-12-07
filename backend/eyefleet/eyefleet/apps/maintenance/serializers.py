from rest_framework import serializers
from eyefleet.apps.maintenance.models.maintenance import (
    MaintenanceType, MaintenanceStatus, MaintenancePriority,
    MaintenanceRequest, Maintenance
)
from eyefleet.apps.maintenance.models.inspections import (
    InspectionType, InspectionStatus, Location, Inspection,
    InspectionField, InspectionResponse, InspectionFieldResponse
)
from eyefleet.apps.maintenance.models.assets import Asset
from eyefleet.apps.maintenance.models.parts import (
    AssetPartType, AssetPartManufacturer, AssetPartSupplier, AssetPart
)

# Maintenance related serializers
class MaintenanceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceType
        fields = '__all__'

class MaintenanceStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceStatus
        fields = '__all__'

class MaintenancePrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenancePriority
        fields = '__all__'

class MaintenanceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceRequest
        fields = '__all__'

class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        fields = '__all__'

# Inspection related serializers
class InspectionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InspectionType
        fields = '__all__'

class InspectionStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = InspectionStatus
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class InspectionFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = InspectionField
        fields = '__all__'

class InspectionFieldResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = InspectionFieldResponse
        fields = '__all__'

class InspectionResponseSerializer(serializers.ModelSerializer):
    field_responses = InspectionFieldResponseSerializer(many=True, read_only=True)

    class Meta:
        model = InspectionResponse
        fields = '__all__'

class InspectionSerializer(serializers.ModelSerializer):
    fields = InspectionFieldSerializer(many=True, read_only=True)
    responses = InspectionResponseSerializer(many=True, read_only=True)

    class Meta:
        model = Inspection
        fields = '__all__'

# Asset related serializers
class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'

# Parts related serializers
class AssetPartTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetPartType
        fields = '__all__'

class AssetPartManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetPartManufacturer
        fields = '__all__'

class AssetPartSupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetPartSupplier
        fields = '__all__'

class AssetPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetPart
        fields = '__all__'