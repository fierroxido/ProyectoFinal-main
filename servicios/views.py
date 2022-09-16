from django.shortcuts import render
from .models import Servicio

# Create your views here.
def verProductos(request):
    return render(request,'servicios.html')