from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import BlogPluginModel

class BlogPlugin(CMSPluginBase):
    model = BlogPluginModel                 # Model where data about this plugin is saved
    name = _("Blog Plugin")                 # Name of the plugin
    render_template = "blog/index.html"   # template to render the plugin with

    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context

plugin_pool.register_plugin(BlogPlugin)
