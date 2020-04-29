from django.db import models
import datetime
import uuid

class User(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    username = models.CharField(max_length=35, blank=False, default='', unique = True)
    email = models.EmailField(unique = True,  default="")
    token = models.UUIDField(default = uuid.uuid4, null = True, editable = False)

    
class HousingHistory(models.Model):
    postcode = models.CharField(max_length=10, blank=False, default='')
    addressLine1 = models.CharField(max_length=35, blank=False, default='')
    addressLine2 = models.CharField(max_length=35, blank=False, default='')
    city = models.CharField(max_length=35, blank=False, default='')
    county = models.CharField(max_length=35, blank=False, default='')
    country = models.CharField(max_length=35, blank=False, default='')
    movingDate = models.DateTimeField()
    user = models.ForeignKey(User, null = True, on_delete=models.CASCADE)

class Email(models.Model):
    to_email = models.EmailField(max_length=50, blank=False, default='')
    subject = models.CharField(max_length=50, blank=False, default='')
    message = models.CharField(max_length=300, blank=False, default='')