# Generated by Django 4.2.6 on 2023-10-28 08:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('drivers', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DriverOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('fromm', models.CharField(max_length=255)),
                ('to', models.CharField(max_length=255)),
                ('time', models.DateTimeField()),
                ('price', models.IntegerField()),
                ('seats', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drivers_order', to='drivers.drivers')),
            ],
            options={
                'verbose_name': 'DriverOrder',
                'verbose_name_plural': 'DriverOrders',
            },
        ),
        migrations.CreateModel(
            name='ClientOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('lat', models.CharField(max_length=255)),
                ('lng', models.CharField(max_length=255)),
                ('is_accepted', models.BooleanField(default=False)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_order', to=settings.AUTH_USER_MODEL)),
                ('driver_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_driver_order', to='drivers.driverorders')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
