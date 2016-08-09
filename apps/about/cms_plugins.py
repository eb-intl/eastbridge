from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import ContentBoxPluginModel
from django.utils.translation import ugettext as _


class ContentBoxPluginPublisher(CMSPluginBase):
    model = ContentBoxPluginModel  # model where plugin data are saved
    module = _("About")
    name = _("About Plugin")  # name of the plugin in the interface
    render_template = "about/plugin/plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(ContentBoxPluginPublisher)
