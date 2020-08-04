from django.contrib import admin

# Register your models here.
from .models import Patient, Donor

admin.site.register(Patient)
admin.site.register(Donor)
