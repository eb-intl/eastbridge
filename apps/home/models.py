from cms.models import CMSPlugin
from cms.utils.compat.dj import python_2_unicode_compatible
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField


@python_2_unicode_compatible
class Section(CMSPlugin):
    """
    """
    title = models.CharField(max_length=512, null=True, blank=True)
    name = models.CharField(max_length=512, null=True, blank=True)
    text = RichTextField(blank=True, null=True)
    shaded = models.BooleanField(default=False)

    def __str__(self):
        return _(u"%s sections") % self.cmsplugin_set.all().count()
