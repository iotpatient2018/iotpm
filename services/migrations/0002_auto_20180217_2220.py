# Generated by Django 2.0.2 on 2018-02-17 16:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='errorlog',
            name='dbErrorTime',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 17, 16, 50, 7, 571383, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ping',
            name='dbTime',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 17, 16, 50, 7, 571383, tzinfo=utc)),
        ),
    ]
