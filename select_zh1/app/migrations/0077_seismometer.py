# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-02 02:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0076_auto_20170501_1658'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seismometer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('protected_obj_distance', models.IntegerField(default=0, null=True)),
                ('blast_transmission_v', models.IntegerField(default=0, null=True)),
                ('blast_shake_hz', models.IntegerField(default=0, null=True)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Create time')),
                ('area', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Area')),
                ('project_blast_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ProjectBlastTypes')),
                ('protected_obj_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ProtectedObjectTypes')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.SysUser')),
            ],
        ),
    ]
