# Generated by Django 4.2.6 on 2023-10-23 12:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.AlterField(
            model_name='users',
            name='phone_number',
            field=models.IntegerField(validators=[django.core.validators.RegexValidator(message='Phone number must be exactly 9 digits long!', regex='^\\d{9}$')]),
        ),
    ]