# Generated by Django 2.2.7 on 2019-11-28 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine_usage', '0009_auto_20191127_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='rin',
            field=models.PositiveIntegerField(blank=True, default=None, null=True, unique=True),
        ),
    ]
