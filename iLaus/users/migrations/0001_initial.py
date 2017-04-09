# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, primary_key=True, serialize=False)),
                ('gender', models.CharField(null=True, blank=True, choices=[('male', '男'), ('female', '女'), ('na', '未知')], max_length=10)),
                ('category', models.CharField(choices=[('stu', '学生'), ('ind', '个人'), ('org', '机构'), ('adm', '管理员'), ('unk', '未知')], max_length=8)),
                ('source', models.CharField(choices=[('site', '网站注册'), ('wechat', '微信注册'), ('admin', '管理员')], max_length=8)),
                ('user_name', models.CharField(blank=True, default='', max_length=100)),
                ('nick_name', models.CharField(blank=True, default='', max_length=100)),
                ('org_name', models.CharField(blank=True, default='', max_length=100)),
                ('mobile_phone', models.CharField(blank=True, max_length=16)),
                ('phone_country', models.CharField(blank=True, max_length=100)),
                ('phone_country_code', models.CharField(blank=True, max_length=100)),
                ('dob', models.DateField(null=True, verbose_name='date of birth', blank=True)),
                ('language', models.CharField(null=True, blank=True, default='chinese', max_length=50)),
                ('description', models.TextField(blank=True, default='', max_length=1000)),
                ('photo_paths', jsonfield.fields.JSONField(default=[])),
                ('profile_paths', jsonfield.fields.JSONField(default=[])),
                ('street_number', models.CharField(null=True, blank=True, max_length=200)),
                ('city', models.CharField(null=True, blank=True, max_length=100)),
                ('state', models.CharField(null=True, blank=True, max_length=100)),
                ('zipcode', models.CharField(null=True, blank=True, max_length=10)),
                ('country', models.CharField(null=True, blank=True, default='CN', max_length=30)),
                ('currency', models.CharField(null=True, blank=True, default='RMB', max_length=20)),
                ('latitude', models.DecimalField(null=True, blank=True, decimal_places=11, max_digits=16)),
                ('longitude', models.DecimalField(null=True, blank=True, decimal_places=11, max_digits=16)),
                ('time_zone_id', models.CharField(null=True, blank=True, max_length=200)),
                ('login_ip', models.GenericIPAddressField(null=True, verbose_name='login IP address', blank=True)),
                ('login_duration', models.DurationField(null=True, verbose_name='last login duration', blank=True)),
                ('signup_platform', models.CharField(null=True, max_length=128)),
                ('created_at', models.DateTimeField(null=True, default=django.utils.timezone.now)),
                ('credit', models.DecimalField(decimal_places=11, default=0, max_digits=16)),
            ],
            options={
                'db_table': 'user_info',
            },
        ),
    ]
