# Generated by Django 2.2.14 on 2020-09-19 18:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20200919_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 19, 18, 0, 34, 519340, tzinfo=utc)),
        ),
    ]