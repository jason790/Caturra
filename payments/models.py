from django.db import models
from django.db.models import Model

# for django cms
from cms.models import CMSPlugin

# Paypal integration
import paypalrestsdk

paypalrestsdk.configure({
    'mode': 'sandbox',
    'client_id': os.environ.get('PAYPAL_CLIENT_ID'),
    'client_id': os.environ.get('PAYPAL_CLIENT_SECRET')
})

class Payment(models.Model):
    def __init__(self):
        pass
