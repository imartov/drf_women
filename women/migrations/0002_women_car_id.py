# Generated by Django 4.1.3 on 2022-11-10 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='women',
            name='car_id',
            field=models.BooleanField(default=True),
        ),
    ]
