# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_auto_20160630_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='industry',
            field=models.CharField(max_length=512, null=True, blank=True),
        ),
    ]
