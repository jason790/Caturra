from django.db import models

# Paypal integration
import paypalrestsdk

paypalrestsdk.configure({
    'mode': 'sandbox',
    'client_id': os.environ.get('PAYPAL_CLIENT_ID'),
    'client_id': os.environ.get('PAYPAL_CLIENT_SECRET')
})

class Payment(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    last_digits = models.CharField(max_length=4)
    gateway = models.CharField(max_length=50)
    status = models.CharField(max_length=20)

    amount = models.IntegerField(default=0)

    created_at = models.DateTimeField('date published')

    def __init__(self):
        pass
