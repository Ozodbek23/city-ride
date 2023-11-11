from rest_framework_simplejwt.authentication import JWTAuthentication
class TelegramUserViewSet(ModelViewSet):
    queryset = TelegramUser.objects.all()
    serializer_class = TelegramUserSerializer

    def get_serializer_class(self):
        if self.action == "verify":
            return SmsVerificationSerializer
        return self.serializer_class

    @action(detail=False, methods=["POST"])
    def verify(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        chat_id = serializer.data.get("chat_id")
        code = serializer.data.get("code")
        tu = TelegramUser.objects.get(chat_id=chat_id)
        if tu.sms == code:
            tu.is_verified = True
            tu.save()
            return Response(status=200)
        return Response(status=400)


class SmsVerificationSerializer(serializers.Serializer):
    code = serializers.IntegerField(required=True)
    chat_id = serializers.IntegerField(required=True)


import random
from django.db import models
from rest_framework.exceptions import ValidationError
from twilio.rest import Client

from rest_framework import serializers

from users.models import TelegramUser, Sms


class TelegramUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = "__all__"

    def create(self, validated_data):
        instance = super(TelegramUserSerializer, self).create(validated_data)
        self.send_sms(telegram_user=instance)
        return instance

    def send_sms(self, telegram_user):
        account_sid = 'AC1114bb3082cdbb9e5825451b211fcdc8'
        auth_token = '93eacd87ac6a001cd485c2c823571b75'
        code = random.randint(111111, 999999)
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=f'You code is: {code}. Do not share it with anyone!',
            from_='+19285698468',
            to='+998333304711'
        )
        print(message.body)

        Sms.objects.create(
            telegram_user=telegram_user,
            sms=code,
        )
