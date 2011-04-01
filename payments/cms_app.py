from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

from .menu import PaymentsMenu
from .menu import SubscriptionsMenu
# from subscriptions.menu import SubscriptionsMenu

class PaymentApp(CMSApp):
    name = _("Payment App")        # give your app a name, this is required
    urls = ["payments.urls"]       # link your app to url configuration(s)
    app_name = "payments"          # this is the application namespace
    menus = [
        PaymentsMenu,
        SubscriptionsMenu,
    ]

apphook_pool.register(PaymentApp)
