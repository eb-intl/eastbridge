from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _

from .models import ServiceGroupPlugin


class ServiceGroupPluginPublisher(CMSPluginBase):
    model = ServiceGroupPlugin  # model where plugin data are saved
    module = _("Services")
    name = _("Services Plugin")  # name of the plugin in the interface
    render_template = "services/snippets/service_group.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(ServiceGroupPluginPublisher)
