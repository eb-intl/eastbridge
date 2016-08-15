# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_office_email'),
        ('blog', '0011_auto_20160810_1915'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlefile',
            options={'verbose_name_plural': 'Files'},
        ),
        migrations.AddField(
            model_name='articlefile',
            name='uploaded_by',
            field=models.ForeignKey(blank=True, to='company.Employee', null=True),
        ),
    ]
