from django.utils.translation import ugettext_lazy as _
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
#from polls_cms_integration.cms_menus import PollsMenu


class ProductApphook(CMSApp):
    name = _("Product Application")
    urls = ["apps.products.urls"]
    app_name = "product"

apphook_pool.register(ProductApphook)