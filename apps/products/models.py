from __future__ import unicode_literals

from django.db import models

from photologue.models import Photo



PRODUCT_TYPES = (
    ('ours', 'Our Products'),
    ('client', 'Client Products'),
)


class Product(models.Model):
    type = models.CharField(max_length=512, choices=PRODUCT_TYPES, blank=True, null=True)
    slug = models.CharField(max_length=512, blank=True, null=True)
    model = models.CharField(max_length=512, blank=True, null=True)
    name = models.CharField(max_length=512, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    image = models.ForeignKey(Photo, related_name='product', blank=True, null=True)
    images = models.ManyToManyField(Photo, related_name='products', blank=True)
    public = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

