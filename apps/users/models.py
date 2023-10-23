from django.db import models

from apps.core.models import TimeStampedModel
from apps.users.choices import UsersRoleChoices
from apps.users.validators import phone_validator


class Users(TimeStampedModel):
    fullname = models.CharField(max_length=255)
    phone_number = models.IntegerField(validators=[phone_validator])
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=50, choices=UsersRoleChoices.choices)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'{self.fullname}'
