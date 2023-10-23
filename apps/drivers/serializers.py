from rest_framework import serializers

from apps.drivers.models import Drivers, CarModels


class DriversSerializers(serializers.ModelSerializer):
    class Meta:
        model = Drivers
        fields = '__all__'


class CarModelsSerializers(serializers.ModelSerializer):
    class Meta:
        model = CarModels
        fields = '__all__'
