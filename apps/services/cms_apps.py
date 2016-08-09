from django.utils.translation import ugettext_lazy as _
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
#from polls_cms_integration.cms_menus import PollsMenu


class ServicesApphook(CMSApp):
    name = _("Services Application")
    urls = ["apps.services.urls"]
    app_name = "services"
    #menus = [PollsMenu]

apphook_pool.register(ServicesApphook)
