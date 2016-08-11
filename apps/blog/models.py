from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from photologue.models import Photo, Gallery
from ckeditor.fields import RichTextField
from filer.fields.file import FilerFileField
from fontawesome.fields import IconField
from cms.models import CMSPlugin


class Tag(models.Model):
    order = models.IntegerField(default=0)
    icon = IconField()
    name = models.CharField(max_length=512, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    visible = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name


class ArticleFile(models.Model):
    slug = models.SlugField(max_length=512, unique=True)
    file = FilerFileField(null=True, blank=True)
    icon = IconField()
    title = models.CharField(max_length=512, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    uploaded_by = models.ForeignKey('company.Employee', blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name='files')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Files'


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
    gallery = models.ManyToManyField(Gallery, blank=True)
    files = models.ManyToManyField(ArticleFile, related_name='articles', blank=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        kwargs = {'year': self.created.year,
                  'month': self.created.month,
                  'day': self.created.day,
                  'slug': self.slug}
        return reverse('blog-detail', kwargs=kwargs)
