from django.utils.translation import ugettext_lazy as _
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
#from polls_cms_integration.cms_menus import PollsMenu


class BlogApphook(CMSApp):
    name = _("Search App")
    urls = ["apps.search.urls"]
    app_name = "search"
    #menus = [PollsMenu]

apphook_pool.register(BlogApphook)