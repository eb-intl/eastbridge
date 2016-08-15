# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0010_auto_20160105_1307'),
        ('clients', '0004_client_industry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testimonial',
            old_name='title',
            new_name='name',
        ),
        migrations.AddField(
            model_name='testimonial',
            name='image',
            field=models.ForeignKey(related_name='testimonial', blank=True, to='photologue.Photo', null=True),
        ),
    ]
