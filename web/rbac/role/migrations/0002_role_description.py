# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-03-25 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('role', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='description',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
