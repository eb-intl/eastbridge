from __future__ import unicode_literals
from django.db import models
from fontawesome.fields import IconField


class Tag(models.Model):
    slug = models.SlugField(max_length=512)
    order = models.IntegerField(default=0)
    icon = IconField()
    short_name = models.CharField(max_length=512, blank=True, null=True)
    long_name = models.CharField(max_length=512, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    visible = models.BooleanField(default=False)

    def __unicode__(self):
        return '{0}-{1}'.format(self.short_name, self.long_name)
