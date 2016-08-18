# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20160816_0809'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='name',
            field=models.CharField(max_length=512, null=True, blank=True),
        ),
    ]
