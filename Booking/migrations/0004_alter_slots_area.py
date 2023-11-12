# Generated by Django 4.2.5 on 2023-11-08 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0003_booking_is_vip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slots',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slots', to='Booking.area'),
        ),
    ]