# Generated by Django 2.2.8 on 2020-01-11 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine_usage', '0013_machinetype_hourly_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='machinetype',
            name='data_entry_after_use',
            field=models.BooleanField(default=False),
        ),
    ]