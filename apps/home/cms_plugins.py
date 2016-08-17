from cms.models import CMSPlugin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .forms import SectionForm
from .models import Section


class SectionsPlugin(CMSPluginBase):
    model = Section
    module = _("Home Page")
    name = _("Section")
    render_template = "home/plugins/sections.html"
    allow_children = True
    child_classes = ['ServiceGroupPluginPublisher',
                     'LatestArticlePluginPublisher',
                     'ClientPluginPublisher',
                     'TeamPluginPublisher',
                     'ContentBoxPluginPublisher',
                     ]
    form = SectionForm

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder,
        })
        return context

    def save_model(self, request, obj, form, change):
        response = super(SectionsPlugin, self).save_model(
            request, obj, form, change
        )
        return response

plugin_pool.register_plugin(SectionsPlugin)
