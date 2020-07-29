from django.db import models
#from localflavor.us.models import USStateField, USZipCodeField


#class Patient(models.Model):
    
    #name = models.CharField(max_length=100),
    #birthday = models.DateField(null=True, blank=True),
    #city = models.CharField(max_length=255),
    #state = USStateField(null=True, blank=True)                       
    #zip_code = USZipCodeField(null=True, blank=True)
    #avatar = models.ImageField(upload_to='static/images', null=True, blank=True)
    #blood_type = models.CharField(max_length=100)
    

class Donor(models.Model):
  name = models.CharField(max_length=100),
  birthday = models.DateField(null=True, blank=True),
  blood_type = models.CharField(max_length=100)