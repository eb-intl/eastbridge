# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_auto_20160808_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicegroup',
            name='processes',
            field=models.ForeignKey(blank=True, to='services.Process', null=True),
        ),
    ]
