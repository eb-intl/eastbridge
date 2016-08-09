from django.utils.translation import ugettext_lazy as _
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
#from polls_cms_integration.cms_menus import PollsMenu


class ClientApphook(CMSApp):
    name = _("Client Application")
    urls = ["apps.clients.urls"]
    app_name = "client"
    #menus = [PollsMenu]

apphook_pool.register(ClientApphook)