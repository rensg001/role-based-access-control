# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-03-04 12:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('role', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, unique=True)),
                ('password', models.CharField(max_length=64)),
                ('solt', models.CharField(max_length=32)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('roles', models.ManyToManyField(related_name='users', to='role.Role')),
            ],
        ),
    ]
