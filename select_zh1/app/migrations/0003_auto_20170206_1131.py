# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20170206_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='short_name',
            field=models.CharField(default='', max_length=100, verbose_name='Short City Name'),
        ),
    ]
