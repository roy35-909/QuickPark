# Generated by Django 4.2.5 on 2023-11-08 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0002_rename_phone_booking_car_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='is_vip',
            field=models.BooleanField(default=False),
        ),
    ]
