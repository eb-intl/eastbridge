# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import fontawesome.fields


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0010_auto_20160105_1307'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.IntegerField(default=0)),
                ('slug', models.CharField(max_length=512, null=True, blank=True)),
                ('name', models.CharField(max_length=512, null=True, blank=True)),
                ('short_description', models.TextField(null=True, blank=True)),
                ('long_description', models.TextField(null=True, blank=True)),
                ('executive', models.BooleanField(default=False)),
                ('image', models.ForeignKey(related_name='employees', to='photologue.Photo')),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.CharField(max_length=512, null=True, blank=True)),
                ('name', models.CharField(max_length=512, null=True, blank=True)),
                ('address', models.TextField(null=True, blank=True)),
                ('telephone', models.CharField(max_length=512, null=True, blank=True)),
                ('email', models.EmailField(max_length=512, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('primary', models.BooleanField(default=False)),
                ('image', models.ForeignKey(related_name='offices', to='photologue.Photo')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=512, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=512, null=True, blank=True)),
                ('link', models.URLField(max_length=512, null=True, blank=True)),
                ('icon', fontawesome.fields.IconField(max_length=60, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.ForeignKey(related_name='employees', to='company.Position'),
        ),
        migrations.AddField(
            model_name='employee',
            name='social',
            field=models.ManyToManyField(related_name='employees', to='company.Social', blank=True),
        ),
    ]
