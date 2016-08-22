# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import fontawesome.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
        ('photologue', '0010_auto_20160105_1307'),
        ('blog', '0002_auto_20160822_0850'),
    ]

    operations = [
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.CharField(max_length=512, null=True, blank=True)),
                ('title', models.CharField(max_length=512, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProcessItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.CharField(max_length=512, null=True, blank=True)),
                ('order', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=512, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.CharField(max_length=512, null=True, blank=True)),
                ('order', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=512, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('text', models.TextField(null=True, blank=True)),
                ('icon', fontawesome.fields.IconField(max_length=60, blank=True)),
                ('image', models.ForeignKey(related_name='services', blank=True, to='photologue.Photo', null=True)),
                ('tags', models.ManyToManyField(related_name='services', to='blog.Tag', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=512, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('process', models.ForeignKey(blank=True, to='services.Process', null=True)),
                ('services', models.ManyToManyField(related_name='groups', to='services.Service', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceGroupPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('service', models.ForeignKey(to='services.ServiceGroup')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AddField(
            model_name='process',
            name='items',
            field=models.ManyToManyField(related_name='process', to='services.ProcessItem', blank=True),
        ),
    ]
