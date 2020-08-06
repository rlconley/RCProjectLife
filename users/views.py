from django.shortcuts import render

from .models import myapp
# Create your views here.

def myapp_detail_view(request):
  obj = Patient.objects.get(id=1)
  context = {


  }

  return render(request, "patient/detail.html", context)