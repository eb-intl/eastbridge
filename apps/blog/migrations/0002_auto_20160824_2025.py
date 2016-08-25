# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
        ('photologue', '0010_auto_20160105_1307'),
        ('metatags', '0001_initial'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlefile',
            name='uploaded_by',
            field=models.ForeignKey(blank=True, to='company.Employee', null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='authors',
            field=models.ManyToManyField(to='company.Employee', blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='files',
            field=models.ManyToManyField(related_name='articles', to='blog.ArticleFile', blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='gallery',
            field=models.ManyToManyField(to='photologue.Gallery', blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ForeignKey(related_name='articles', blank=True, to='photologue.Photo', null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(related_name='articles', to='metatags.Tag'),
        ),
    ]
