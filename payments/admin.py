from django.contrib import admin

from .models import Payment
from .models import Subscription

# Register your models here.
admin.site.register(Payment)
admin.site.register(Subscription)
