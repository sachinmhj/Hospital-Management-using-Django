from django.db import models

# Create your models here.
class HospitalRecord(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField()
    website = models.URLField()
    capacity = models.IntegerField()