from django.db import models
from django import forms

# Create your models here.
class Add(models.Model):
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pincode = models.CharField(max_length=6)
    country = models.CharField(max_length=20)