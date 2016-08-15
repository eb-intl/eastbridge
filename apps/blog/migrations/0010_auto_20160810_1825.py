# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20160810_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlefile',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='articlefile',
            name='slug',
            field=models.SlugField(default='-', unique=True, max_length=512),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articlefile',
            name='tags',
            field=models.ManyToManyField(related_name='files', to='blog.Tag'),
        ),
        migrations.AddField(
            model_name='articlefile',
            name='title',
            field=models.CharField(max_length=512, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='visible',
            field=models.BooleanField(default=False),
        ),
    ]
