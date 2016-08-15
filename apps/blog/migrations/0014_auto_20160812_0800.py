# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20160812_0757'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='long_name',
            field=models.CharField(max_length=512, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(default='-slug-', max_length=512),
            preserve_default=False,
        ),
    ]
