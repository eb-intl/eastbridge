# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import fontawesome.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20160810_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlefile',
            name='icon',
            field=fontawesome.fields.IconField(max_length=60, blank=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='icon',
            field=fontawesome.fields.IconField(max_length=60, blank=True),
        ),
    ]
