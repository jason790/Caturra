from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from cms.menu_bases import CMSAttachMenu
from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool

from .models import Payment
from .models import Subscription

class PaymentsMenu(CMSAttachMenu):
    name = _("Payments Menu") # give the menu a name, this is required.

    def get_nodes(self, request):
        """
        This method is used to build the menu tree.
        """
        nodes = []
        for payment in Payment.objects.all():
            # the menu tree consists of NavigationNode instances
            # Each NavigationNode takes a label as its first argument, a URL as
            # its second argument and a (for this tree) unique id as its third
            # argument.
            node = NavigationNode(
                payment.name,
                reverse('payment:description', args=(payment.pk,)),
                payment.id
            )
            nodes.append(node)
        return nodes

menu_pool.register_menu(PaymentsMenu)

class SubscriptionsMenu(CMSAttachMenu):
    name = _("Subscription Menu") # give the menu a name, this is required.

    def get_nodes(self, request):
        """
        This method is used to build the menu tree.
        """
        # the menu tree consists of NavigationNode instances
        # Each NavigationNode takes a label as its first argument, a URL as
        # its second argument and a (for this tree) unique id as its third
        # argument.
        nodes = [
            NavigationNode(
                "Bronze",
                "Bronze Plan",
                1
            ),
            NavigationNode(
                "Silver",
                "Silver Plan",
                2
            ),
            NavigationNode(
                "Gold",
                "Gold Plan",
                3
            ),
        ]

        for subscription in Subscription.objects.all():
            node = NavigationNode(
                subscription.name,
                reverse('subscription:description', args=(subscription.pk,)),
                subscription.id
            )
            nodes.append(node)

        return nodes

menu_pool.register_menu(SubscriptionsMenu)
