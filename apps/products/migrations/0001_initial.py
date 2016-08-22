# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0010_auto_20160105_1307'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(blank=True, max_length=512, null=True, choices=[('ours', 'Our Products'), ('client', 'Client Products')])),
                ('slug', models.CharField(max_length=512, null=True, blank=True)),
                ('model', models.CharField(max_length=512, null=True, blank=True)),
                ('name', models.CharField(max_length=512, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('body', models.TextField(null=True, blank=True)),
                ('public', models.BooleanField(default=True)),
                ('image', models.ForeignKey(related_name='product', blank=True, to='photologue.Photo', null=True)),
                ('images', models.ManyToManyField(related_name='products', to='photologue.Photo', blank=True)),
            ],
        ),
    ]
