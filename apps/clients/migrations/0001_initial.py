# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0010_auto_20160105_1307'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.CharField(max_length=512, null=True, blank=True)),
                ('name', models.CharField(max_length=512, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('industry', models.CharField(max_length=512, null=True, blank=True)),
                ('link', models.URLField(max_length=512, null=True, blank=True)),
                ('private', models.BooleanField(default=True)),
                ('image', models.ForeignKey(related_name='client', blank=True, to='photologue.Photo', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=512, null=True, blank=True)),
                ('text', models.TextField(null=True, blank=True)),
                ('public', models.BooleanField(default=True)),
                ('image', models.ForeignKey(related_name='testimonial', blank=True, to='photologue.Photo', null=True)),
            ],
        ),
    ]
