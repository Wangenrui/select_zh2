# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 05:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_auto_20170213_0504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipemntsubtype',
            name='type',
        ),
        migrations.DeleteModel(
            name='Equipment',
        ),
        migrations.DeleteModel(
            name='EquipemntSubType',
        ),
        migrations.DeleteModel(
            name='EquipmentType',
        ),
    ]
