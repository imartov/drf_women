# Generated by Django 4.1.3 on 2022-11-13 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0006_remove_women_categor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='women',
            name='car_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='women.category'),
        ),
    ]
