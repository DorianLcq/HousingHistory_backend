from django.db import models

 
class HousingHistory(models.Model):
    postcode = models.CharField(max_length=10, blank=False, default='')
    addressLine1 = models.CharField(max_length=35, blank=False, default='')
    addressLine2 = models.CharField(max_length=35, blank=False, default='')
    city = models.CharField(max_length=35, blank=False, default='')
    county = models.CharField(max_length=35, blank=False, default='')
    country = models.CharField(max_length=35, blank=False, default='')
    movingDate = models.DateTimeField()
