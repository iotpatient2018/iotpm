# Generated by Django 2.0.2 on 2018-02-18 05:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogDataMonit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dbLogTime', models.DateTimeField()),
                ('dbTemp', models.IntegerField(default=0)),
                ('dbHumid', models.IntegerField(default=0)),
                ('dbHeartb', models.IntegerField(default=0)),
                ('dbBuzState', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='LogErrorMonit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dbErrorMonit', models.CharField(max_length=500)),
                ('dbErrorTimeMonit', models.DateTimeField(default=datetime.datetime(2018, 2, 18, 5, 51, 10, 955100, tzinfo=utc))),
                ('dbErrorCodeMonit', models.CharField(max_length=500)),
            ],
        ),
    ]