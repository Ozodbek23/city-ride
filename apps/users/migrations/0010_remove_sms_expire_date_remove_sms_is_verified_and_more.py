# Generated by Django 4.2.6 on 2023-11-07 14:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_user_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sms',
            name='expire_date',
        ),
        migrations.RemoveField(
            model_name='sms',
            name='is_verified',
        ),
        migrations.AddField(
            model_name='sms',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 7, 14, 8, 32, 140227, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='sms',
            name='is_used',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(default=False, verbose_name='verified'),
        ),
    ]
