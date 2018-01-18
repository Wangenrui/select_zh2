# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 05:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_remove_equipment_company_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='company',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Company'),
        ),
    ]
