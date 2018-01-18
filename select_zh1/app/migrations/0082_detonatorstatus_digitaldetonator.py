# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-24 01:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0081_area_equipment'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetonatorStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DigitalDetonator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.DecimalField(decimal_places=7, default=0.0, max_digits=10, verbose_name='Longitude')),
                ('latitude', models.DecimalField(decimal_places=7, default=0.0, max_digits=10, verbose_name='Latitude')),
                ('blast_time', models.DateField(default=django.utils.timezone.now, verbose_name='Blast time')),
                ('code', models.CharField(default='', max_length=32, null=True, verbose_name='Code')),
                ('company_code', models.CharField(default='', max_length=10, null=True, verbose_name='Company Code')),
                ('special_code', models.CharField(default='', max_length=10, null=True, verbose_name='Special Code')),
                ('serial_code', models.CharField(default='', max_length=10, null=True, verbose_name='Serial Code')),
                ('manu_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Create time')),
                ('status', models.SmallIntegerField(default=0, null=True)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Create time')),
                ('area', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Area')),
                ('equipment', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Equipment')),
                ('user', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='app.SysUser')),
            ],
        ),
    ]