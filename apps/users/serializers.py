from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from apps.users.models import User


class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'full_name', 'phone_number', 'role']


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['full_name', 'phone_number', 'role']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        instance = User.objects.create(**validated_data)
        return instance
