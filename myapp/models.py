from django.db import models
from users.models import User

# from localflavor import USStateField, USZipCodeField


class Patient(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=255)
    # state = USStateField(null=True, blank=True)                  
    # zip_code = USZipCodeField(null=True, blank=True)
    avatar = models.ImageField(upload_to='static/images', null=True, blank=True)
    blood_type = models.CharField(max_length=100)
    hospital = models.CharField(max_length=100)
    need = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Donor(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    blood_type = models.CharField(max_length=100)
    donation_type = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

