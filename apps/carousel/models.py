from __future__ import unicode_literals

from django.db import models
from django.contrib.sites.models import Site

from photologue.models import Photo


class Layer(models.Model):
    order = models.IntegerField(default=0)
    body = models.TextField(blank=True, null=True)
    start = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name


class Slide(models.Model):
    order = models.IntegerField(default=0)
    title = models.CharField(max_length=512, blank=True, null=True)
    image = models.ForeignKey(Photo, related_name='slides')

    def __unicode__(self):
        return self.name

