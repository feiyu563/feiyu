# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-18 09:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0002_auto_20170718_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moniter_task',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='moniter_task',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]