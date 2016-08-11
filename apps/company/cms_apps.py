from django.utils.translation import ugettext_lazy as _
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
#from polls_cms_integration.cms_menus import PollsMenu


class CompanyApphook(CMSApp):
    name = _("Company Application")
    urls = ["apps.company.urls"]
    app_name = "company"

apphook_pool.register(CompanyApphook)


class TeamApphook(CMSApp):
    name = _("Team Application")
    urls = ["apps.company.team_urls"]
    app_name = "team"

apphook_pool.register(TeamApphook)
