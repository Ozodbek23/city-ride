# Generated by Django 4.2.6 on 2023-11-09 14:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_sms_expires_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sms',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 9, 14, 46, 2, 219069, tzinfo=datetime.timezone.utc)),
        ),
    ]
