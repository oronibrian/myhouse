from rest_framework.serializers import ModelSerializer
from .models import Building,Property, Tenant


class BuildingSerializer(ModelSerializer):
    class Meta:
        model=Building
        fields=[
            'id',
            'name',
            'notes',

        ]


class PropertySerializer(ModelSerializer):
    class Meta:
        model=Property
        fields=[
            'id',
            'name',
            'building',
            'address',
            'notes',
            'area',
            'rooms',

        ]

class TenantSerializer(ModelSerializer):
    class Meta:
        model=Tenant
        fields=[
            'id',
            'name',
            'tenancy_begin_date',
            'tenancy_end_date',
            'deposit',
            'contact_info',


        ]


