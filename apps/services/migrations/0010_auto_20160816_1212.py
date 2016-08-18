# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
        ('services', '0009_serviceplugin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serviceplugin',
            name='cmsplugin_ptr',
        ),
        migrations.RemoveField(
            model_name='serviceplugin',
            name='service',
        ),
        migrations.DeleteModel(
            name='ServicePlugin',
        ),
    ]
