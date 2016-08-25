from __future__ import unicode_literals

from django.db import models
from photologue.models import Photo


class Testimonial(models.Model):
    name = models.CharField(max_length=512, blank=True, null=True)
    image = models.ForeignKey(
        Photo, related_name='testimonial', blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    public = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class Client(models.Model):
    slug = models.CharField(max_length=512, blank=True, null=True)
    name = models.CharField(max_length=512, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    industry = models.CharField(max_length=512, blank=True, null=True)
    link = models.URLField(max_length=512, blank=True, null=True)
    image = models.ForeignKey(Photo, related_name='client', blank=True, null=True)
    # country
    # city
    private = models.BooleanField(default=True)
    products = models.ManyToManyField(
        'products.Product', related_name='clients', blank=True)
    tags = models.ManyToManyField('metatags.Tag', related_name='clients', blank=True)
    testimonials = models.ManyToManyField(
        Testimonial, related_name='clients', blank=True)

    def __unicode__(self):
        return self.name
