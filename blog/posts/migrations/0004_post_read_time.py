# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-02 15:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20170429_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='read_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
