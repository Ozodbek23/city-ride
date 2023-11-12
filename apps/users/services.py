import os

from dotenv import load_dotenv
from twilio.rest import Client

from apps.users.exceptions import ExpireActivationCodeException
from apps.users.models import SMS

load_dotenv()


def send_sms(phone_number, code):
    account_sid = os.getenv('account_sid')
    auth_token = os.getenv('auth_token')
    from_number = os.getenv('from_')
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f'You code is: {code}. Do not share it with anyone!',
        from_=f'{from_number}',
        to=f'+998{phone_number}'
    )
    print(message.body)


def check_activation_code(phone_number, code):
    activation_code = SMS.objects.filter(phone_number=phone_number, is_used=False).last()
    if activation_code:
        if activation_code.expired:
            raise ExpireActivationCodeException
        if activation_code.code == code:
            activation_code.is_used = True
            activation_code.save(update_fields=["is_used"])
            return True
        return False
