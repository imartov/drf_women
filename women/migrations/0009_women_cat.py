# Generated by Django 4.1.3 on 2022-11-13 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0008_alter_women_car_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='women',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='women.category'),
        ),
    ]
