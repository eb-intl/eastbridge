from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _

from .models import Client


class ClientPluginPublisher(CMSPluginBase):
    module = _("Client")
    name = _("Client Carousel")
    render_template = "clients/snippets/carousel.html"

    def render(self, context, instance, placeholder):
        clients = Client.objects.filter(private=False)
        context.update({'clients': clients})
        return context

plugin_pool.register_plugin(ClientPluginPublisher)
