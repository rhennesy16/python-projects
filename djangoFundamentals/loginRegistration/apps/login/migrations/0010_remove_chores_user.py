# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-22 20:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_auto_20181022_1214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chores',
            name='user',
        ),
    ]
