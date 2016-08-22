# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.file
import fontawesome.fields
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0006_auto_20160623_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_created=True)),
                ('slug', models.SlugField(unique=True, max_length=512)),
                ('title', models.CharField(max_length=512, null=True, blank=True)),
                ('subtitle', models.CharField(max_length=512, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('body', ckeditor.fields.RichTextField(null=True, blank=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('publish', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True, max_length=512)),
                ('icon', fontawesome.fields.IconField(max_length=60, blank=True)),
                ('title', models.CharField(max_length=512, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('file', filer.fields.file.FilerFileField(blank=True, to='filer.File', null=True)),
            ],
            options={
                'verbose_name_plural': 'Files',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(max_length=512)),
                ('order', models.IntegerField(default=0)),
                ('icon', fontawesome.fields.IconField(max_length=60, blank=True)),
                ('short_name', models.CharField(max_length=512, null=True, blank=True)),
                ('long_name', models.CharField(max_length=512, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('visible', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='articlefile',
            name='tags',
            field=models.ManyToManyField(related_name='files', to='blog.Tag'),
        ),
    ]
