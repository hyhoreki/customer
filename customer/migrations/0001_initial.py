# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 02:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('sex', models.IntegerField(default=0)),
                ('phone', models.IntegerField(default=0)),
                ('age', models.IntegerField(default=0)),
                ('job', models.TextField(default='未知')),
                ('money', models.IntegerField(default=0)),
                ('hobby', models.TextField(default='未知')),
                ('house', models.IntegerField(default='未知')),
                ('contact', models.TextField(default='尽快开始接触哦')),
            ],
        ),
    ]
