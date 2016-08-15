# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_office_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='office',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
    ]
