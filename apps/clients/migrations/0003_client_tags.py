# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metatags', '0001_initial'),
        ('clients', '0002_auto_20160824_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='tags',
            field=models.ManyToManyField(related_name='clients', to='metatags.Tag', blank=True),
        ),
    ]
