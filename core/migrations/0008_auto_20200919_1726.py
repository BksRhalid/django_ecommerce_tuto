# Generated by Django 2.2.14 on 2020-09-19 17:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200918_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 19, 17, 26, 42, 807417, tzinfo=utc)),
        ),
    ]
