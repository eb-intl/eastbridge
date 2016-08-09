from __future__ import unicode_literals

from django.db import models
from django.contrib.sites.models import Site

from photologue.models import Photo


class Layer(models.Model):
    order = models.IntegerField(default=0)
    slug = models.CharField(max_length=512, blank=True, null=True)
    name = models.CharField(max_length=512, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ForeignKey(Photo, related_name='employees')
    featured = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name


class Slide(models.Model):
    sites = models.ManyToManyField(Site)
    order = models.IntegerField(default=0)
    slug = models.CharField(max_length=512, blank=True, null=True)
    name = models.CharField(max_length=512, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ForeignKey(Photo, related_name='employees')
    featured = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

