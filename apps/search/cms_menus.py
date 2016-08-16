from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from cms.menu_bases import CMSAttachMenu
from menus.base import NavigationNode
from menus.menu_pool import menu_pool


"""
class PollsMenu(CMSAttachMenu):
    name = _("News Articles")  # give the menu a name this is required.

    def get_nodes(self, request):
        nodes = []

        # loop over all the Poll objects in the database
        for poll in Poll.objects.all():

            # create a NavigationNode based on each one
            node = NavigationNode(
                title=poll.question,
                url=reverse('polls:detail', args=(poll.pk,)),
                id=poll.pk,
            )
            nodes.append(node)
        return nodes

menu_pool.register_menu(PollsMenu)
"""

