# Generated by Django 4.2.6 on 2023-11-09 14:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_remove_sms_expire_date_remove_sms_is_verified_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sms',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 9, 14, 16, 47, 698314, tzinfo=datetime.timezone.utc)),
        ),
    ]
