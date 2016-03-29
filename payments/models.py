from django.db import models
import paypalrestsdk

paypalrestsdk.configure({
    'mode': 'sandbox',
    'client_id': os.environ.get('PAYPAL_CLIENT_ID'),
    'client_id': os.environ.get('PAYPAL_CLIENT_SECRET')
})
