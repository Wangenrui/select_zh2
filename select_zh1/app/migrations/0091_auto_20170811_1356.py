# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-11 13:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0090_auto_20170810_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='menu_addr',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='select_sysuser',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Select_Role'),
        ),
    ]
