from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

from .menu import UsersMenu

class UserApp(CMSApp):
    name = _("Users App")        # give your app a name, this is required
    # urls = ["user.urls"]       # link your app to url configuration(s)
    app_name = "users"          # this is the application namespace
    menus = [UsersMenu,]

apphook_pool.register(UserApp)
