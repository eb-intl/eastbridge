# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.file


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0006_auto_20160623_1627'),
        ('blog', '0008_article_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', filer.fields.file.FilerFileField(blank=True, to='filer.File', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='files',
            field=models.ManyToManyField(related_name='articles', to='blog.ArticleFile', blank=True),
        ),
    ]
