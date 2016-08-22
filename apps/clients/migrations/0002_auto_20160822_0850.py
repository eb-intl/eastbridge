# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='products',
            field=models.ManyToManyField(related_name='clients', to='products.Product', blank=True),
        ),
        migrations.AddField(
            model_name='client',
            name='testimonials',
            field=models.ManyToManyField(related_name='clients', to='clients.Testimonial', blank=True),
        ),
    ]
