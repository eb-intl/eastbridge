# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import fontawesome.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
        ('sites', '0001_initial'),
        ('photologue', '0010_auto_20160105_1307'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentBox',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=512, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('icon', fontawesome.fields.IconField(max_length=60, blank=True)),
                ('sites', models.ManyToManyField(to='sites.Site')),
            ],
        ),
        migrations.CreateModel(
            name='ContentBoxPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('content_box', models.ForeignKey(to='about.ContentBox')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='TextBox',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=512, null=True, blank=True)),
                ('body', models.TextField(null=True, blank=True)),
                ('image', models.ForeignKey(related_name='textboxes', to='photologue.Photo')),
                ('sites', models.ManyToManyField(to='sites.Site')),
            ],
        ),
    ]
