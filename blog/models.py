from django.db import models


# Create your models here.

class Country(models.Model):
    country = models.CharField(max_length=30)
    capital = models.CharField(max_length=30)
    region = models.CharField(max_length=40)
    time_create = models.DateTimeField(auto_now_add=True)


