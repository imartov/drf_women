# Generated by Django 4.1.3 on 2022-11-12 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0002_women_car_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='women',
            name='car_id',
        ),
    ]
