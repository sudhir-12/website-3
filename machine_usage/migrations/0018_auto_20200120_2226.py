# Generated by Django 2.2.8 on 2020-01-21 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine_usage', '0017_usage_clear_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_graduating',
            field=models.BooleanField(default=False),
        ),
    ]
