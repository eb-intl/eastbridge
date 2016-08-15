# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0010_auto_20160105_1307'),
        ('blog', '0007_auto_20160808_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='gallery',
            field=models.ManyToManyField(to='photologue.Gallery', blank=True),
        ),
    ]
