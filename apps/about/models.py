from __future__ import unicode_literals

from django.db import models
from django.contrib.sites.models import Site
from fontawesome.fields import IconField
from photologue.models import Photo


class ContentBox(models.Model):
    sites = models.ManyToManyField(Site)
    order = models.IntegerField(default=0)
    title = models.CharField(max_length=512, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    icon = IconField()

    def __unicode__(self):
        return self.title


class TextBox(models.Model):
    sites = models.ManyToManyField(Site)
    order = models.IntegerField(default=0)
    title = models.CharField(max_length=512, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    image = models.ForeignKey(Photo, related_name='textboxes')

    def __unicode__(self):
        return self.title
