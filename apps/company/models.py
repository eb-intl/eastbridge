from __future__ import unicode_literals

from django.db import models
from fontawesome.fields import IconField
from photologue.models import Photo
from cms.models import CMSPlugin


class Social(models.Model):
    order = models.IntegerField(default=0)
    name = models.CharField(max_length=512, blank=True, null=True)
    link = models.URLField(max_length=512, blank=True, null=True)
    icon = IconField()

    def __unicode__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=512, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name


class Employee(models.Model):
    order = models.IntegerField(default=0)
    slug = models.CharField(max_length=512, blank=True, null=True)
    name = models.CharField(max_length=512, blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    position = models.ForeignKey(Position, related_name='employees')
    image = models.ForeignKey(Photo, related_name='employees')
    social = models.ManyToManyField(Social, related_name='employees',
                               blank=True)
    executive = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name


class Office(models.Model):
    slug = models.CharField(max_length=512, blank=True, null=True)
    name = models.CharField(max_length=512, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    telephone = models.CharField(max_length=512, blank=True, null=True)
    email = models.EmailField(max_length=512, blank=True, null=True)
    #country
    #city
    image = models.ForeignKey(Photo, related_name='offices')
    primary = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name



