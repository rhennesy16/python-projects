# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-22 19:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_chores'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chores',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Users'),
        ),
    ]
