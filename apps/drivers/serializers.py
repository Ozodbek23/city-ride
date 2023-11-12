from random import randint

from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from apps.drivers.models import Drivers, CarModels
from apps.users.choices import UsersRoleChoices
from apps.users.models import User, SMS
from apps.users.services import send_sms


class DriversSerializers(serializers.ModelSerializer):
    class Meta:
        model = Drivers
        fields = '__all__'


class DriverListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drivers
        fields = [
            'user',
            'car_model',
            'car_photo',
        ]


class DriverCreateSerializer(serializers.ModelSerializer):
    car_model = serializers.IntegerField(write_only=True)
    car_photo = serializers.ImageField(write_only=True)
    car_number = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['car_model', 'car_photo', 'car_number', 'full_name', 'phone_number', 'password']

    def create(self, validated_data):
        phone_number = validated_data['phone_number']
        code = randint(111111, 999999)
        send_sms(phone_number, code)
        SMS.objects.create(phone_number=phone_number, code=code)
        validated_data['password'] = make_password(validated_data['password'])
        validated_data['role'] = UsersRoleChoices.DRIVER.value
        car_model = validated_data.pop('car_model')
        car_photo = validated_data.pop('car_photo')
        car_number = validated_data.pop('car_number')
        instance = User.objects.create(**validated_data)
        Drivers.objects.create(
            user=instance,
            car_model_id=car_model,
            car_photo=car_photo,
            car_number=car_number,
        )
        return instance


class DriverDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drivers
        fields = [
            'car_model',
            'car_number',
            'car_photo'
        ]

    def get_user(self):
        user = self.context['request.user']


class DriverUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drivers
        fields = ['car_number', 'car_photo']


class CarModelsSerializers(serializers.ModelSerializer):
    class Meta:
        model = CarModels
        fields = '__all__'
