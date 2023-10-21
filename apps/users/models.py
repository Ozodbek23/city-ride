from django.db import models

from apps.core.models import TimeStampedModel
from apps.users.choices import UsersRoleChoices


class Users(TimeStampedModel):
    fullname = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=50, choices=UsersRoleChoices.choices)
