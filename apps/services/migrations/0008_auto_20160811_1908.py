# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_servicegroupplugin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicegroup',
            old_name='processes',
            new_name='process',
        ),
    ]
