# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-23 08:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20170423_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='brief',
            field=models.CharField(default='some string', max_length=100),
        ),
    ]
