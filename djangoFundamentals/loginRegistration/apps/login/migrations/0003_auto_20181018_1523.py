# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-18 22:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20181018_1423'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='users',
        ),
        migrations.AddField(
            model_name='comments',
            name='message',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='login.Messages'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='login.Users'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='messages',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='message', to='login.Users'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='messages',
            name='message',
            field=models.CharField(max_length=255),
        ),
    ]
