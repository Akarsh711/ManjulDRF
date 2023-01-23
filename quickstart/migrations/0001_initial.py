# Generated by Django 3.1 on 2023-01-23 18:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('done', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(default=datetime.datetime(2023, 1, 24, 0, 28, 44, 391168))),
            ],
        ),
    ]