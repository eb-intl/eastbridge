# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_auto_20160629_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='office',
            name='email',
            field=models.EmailField(max_length=512, null=True, blank=True),
        ),
    ]
