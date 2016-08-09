from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _

from .models import Article


class LatestArticlePluginPublisher(CMSPluginBase):
    #model = ServiceGroupPlugin
    module = _("Article")
    name = _("Lastest Articles Plugin")
    render_template = "blog/snippets/latest.html"

    def render(self, context, instance, placeholder):
        latest = Article.objects.filter().order_by('created')[:3]
        context.update({'latest_news': latest})
        return context

plugin_pool.register_plugin(LatestArticlePluginPublisher)
