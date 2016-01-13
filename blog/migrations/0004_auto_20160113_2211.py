# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-01-13 16:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160113_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dwn',
            field=models.CharField(default=datetime.datetime(2016, 1, 13, 16, 41, 26, 850887, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='artist',
            field=models.CharField(blank=True, default='unknown', max_length=30),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(),
        ),
    ]