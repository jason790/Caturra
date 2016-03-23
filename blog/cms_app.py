from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

from .menu import PostsMenu

class BlogApp(CMSApp):
    name = _("Blog App")        # give your app a name, this is required
    urls = ["blog.urls"]       # link your app to url configuration(s)
    app_name = "blog"          # this is the application namespace

apphook_pool.register(BlogApp)
