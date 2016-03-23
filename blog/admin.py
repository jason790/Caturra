from django.contrib import admin

# from adminsortable.admin import SortableAdmin, SortableTabularInline
# from cms.admin.placeholderadmin import PlaceholderAdminMixin
# from easy_select2 import select2_modelform
from .models import Post

# Register your models here.
admin.site.register(Post)
