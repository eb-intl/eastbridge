# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20160812_0800'),
        ('services', '0010_auto_20160816_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='tags',
            field=models.ManyToManyField(related_name='services', to='blog.Tag', blank=True),
        ),
    ]
