# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_auto_20160808_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='processitem',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='service',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='servicegroup',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]
