# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import fontawesome.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
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
    ]
