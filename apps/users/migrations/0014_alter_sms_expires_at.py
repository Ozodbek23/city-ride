# Generated by Django 4.2.6 on 2023-11-25 12:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_alter_sms_code_alter_sms_expires_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sms',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 25, 12, 38, 52, 896393, tzinfo=datetime.timezone.utc)),
        ),
    ]
