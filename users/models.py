from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    picture = models.CharField(max_length=20)
    description = models.CharField(max_length=20)

    email = models.CharField(max_length=80)
    password = models.CharField(max_length=140)

    gender = models.CharField(max_length=6)
    birth = models.DateTimeField('date birth')

    subscription = models.CharField(max_length=20)

    created_at = models.DateTimeField('date created')
    updated_at = models.DateTimeField('date updated')
