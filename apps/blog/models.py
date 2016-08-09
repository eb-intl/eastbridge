from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from photologue.models import Photo
from ckeditor.fields import RichTextField
from cms.models import CMSPlugin


class Tag(models.Model):
    order = models.IntegerField(default=0)
    name = models.CharField(max_length=512, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name


class Article(models.Model):
    slug = models.SlugField(max_length=512, unique=True)
    title = models.CharField(max_length=512, blank=True, null=True)
    subtitle = models.CharField(max_length=512, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    created = models.DateTimeField(auto_created=True)
    updated = models.DateTimeField(auto_now_add=True)
    publish = models.BooleanField(default=False)

    image = models.ForeignKey(Photo, related_name='articles', blank=True, null=True)
    authors = models.ManyToManyField('company.Employee', blank=True)
    tags = models.ManyToManyField(Tag, related_name='articles')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        kwargs = {'year': self.created.year,
                  'month': self.created.month,
                  'day': self.created.day,
                  'slug': self.slug}
        return reverse('blog-detail', kwargs=kwargs)
