# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MsgPhone',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('auth_code', models.CharField(blank=True, max_length=15)),
                ('mobile_phone', models.CharField(blank=True, max_length=16)),
                ('phone_country', models.CharField(blank=True, max_length=100, default='china')),
                ('phone_country_code', models.CharField(blank=True, max_length=100, default='+86')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('credit', models.DecimalField(max_digits=16, decimal_places=11, default=0)),
                ('exprit_time', models.DateTimeField(default=datetime.datetime(2017, 4, 13, 14, 11, 0, 561761, tzinfo=utc))),
            ],
            options={
                'db_table': 'msg_phone',
            },
        ),
    ]
