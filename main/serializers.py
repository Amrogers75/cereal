from main.models import Cereal, Manufacturer
from rest_framework import serializers


class CerealSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cereal
        fields = ('name', 'calories', 'sugars',)


class ManufacturerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ('name',)