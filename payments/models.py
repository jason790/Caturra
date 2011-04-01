import os
from django.db import models

from users.models import User

# Paypal integration
import paypalrestsdk

class Subscription(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    price = models.IntegerField(default=0)

    created_at = models.DateTimeField('date created')
    updated_at = models.DateTimeField('date updated')

class Payment(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User)
    description = models.CharField(max_length=255)

    last_digits = models.CharField(max_length=4)
    gateway = models.CharField(max_length=50)
    status = models.CharField(max_length=20)

    amount = models.IntegerField(default=0)

    created_at = models.DateTimeField('date published')

    # def __init__(self):
    #     paypalrestsdk.configure({
    #         'mode': 'sandbox',
    #         'client_id': os.environ.get('PAYPAL_CLIENT_ID'),
    #         'client_secret': os.environ.get('PAYPAL_CLIENT_SECRET')
    #     })
    #
    #     super

    def __str__(self):
        return self.name
