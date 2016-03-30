from django.db import models

# Create your models here.
class Subscription(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    price = models.IntegerField(default=0)

    created_at = models.DateTimeField('date created')
    updated_at = models.DateTimeField('date updated')
