# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-29 22:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20160629_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='social',
            field=models.ManyToManyField(blank=True, related_name='employees', to='company.Social'),
        ),
    ]
