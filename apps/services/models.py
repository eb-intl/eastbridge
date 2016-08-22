from __future__ import unicode_literals

from django.db import models
from django.contrib.sites.models import Site
from fontawesome.fields import IconField
from photologue.models import Photo
from cms.models import CMSPlugin


class ProcessItem(models.Model):
    slug = models.CharField(max_length=512, blank=True, null=True)
    order = models.IntegerField(default=0)
    title = models.CharField(max_length=512, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.title


class Process(models.Model):
    slug = models.CharField(max_length=512, blank=True, null=True)
    title = models.CharField(max_length=512, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    items = models.ManyToManyField(
        ProcessItem, related_name='process', blank=True)

    def __unicode__(self):
        return self.title


class Service(models.Model):
    slug = models.CharField(max_length=512, blank=True, null=True)
    order = models.IntegerField(default=0)
    title = models.CharField(max_length=512, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    image = models.ForeignKey(
        Photo, related_name='services', blank=True, null=True)
    icon = IconField()
    tags = models.ManyToManyField('metatags.Tag', related_name='services', blank=True)

    def __unicode__(self):
        return self.title


class ServiceGroup(models.Model):
    order = models.IntegerField(default=0)
    title = models.CharField(max_length=512, blank=True, null=True)
    services = models.ManyToManyField(
        Service, related_name='groups', blank=True)
    process = models.ForeignKey(Process, blank=True, null=True)
    tags = models.ManyToManyField('metatags.Tag', related_name='service_groups', blank=True)

    def __unicode__(self):
        return self.title


class ServiceGroupPlugin(CMSPlugin):
    service = models.ForeignKey(ServiceGroup)

    def __unicode__(self):
        return self.service.title