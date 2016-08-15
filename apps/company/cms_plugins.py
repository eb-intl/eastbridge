from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _

from .models import Employee


class TeamPluginPublisher(CMSPluginBase):
    module = _("Company")
    name = _("Team Plugin")
    render_template = "company/plugins/team.html"

    def render(self, context, instance, placeholder):
        executives = Employee.objects.filter(executive=True)
        context.update({'executives': executives})
        return context

plugin_pool.register_plugin(TeamPluginPublisher)
