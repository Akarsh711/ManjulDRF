# Generated by Django 3.1 on 2023-01-23 20:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0004_auto_20230124_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2023, 1, 24, 1, 46, 48, 622968)),
        ),
    ]
