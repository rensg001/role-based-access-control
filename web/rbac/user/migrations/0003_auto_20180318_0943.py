# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-03-18 09:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20180304_1238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='solt',
            new_name='salt',
        ),
    ]
