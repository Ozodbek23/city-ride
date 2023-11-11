from random import randint

from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from apps.drivers.models import Drivers
from apps.users.models import User, SMS
from apps.users.services import send_sms


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'full_name', 'phone_number', 'role', 'is_verified']


class UsersDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'full_name', 'phone_number', 'role', 'is_verified', 'is_active', 'is_staff', 'is_superuser',
                  'created_at', 'updated_at']


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'full_name',
            'phone_number'
        ]


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['full_name', 'phone_number', 'password']

    def create(self, validated_data):
        phone_number = validated_data['phone_number']
        code = randint(111111, 999999)
        send_sms(phone_number, code)
        SMS.objects.create(phone_number=phone_number, code=code)
        validated_data['password'] = make_password(validated_data['password'])
        instance = User.objects.create(**validated_data)
        return instance


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'full_name',
            'phone_number',
        ]
