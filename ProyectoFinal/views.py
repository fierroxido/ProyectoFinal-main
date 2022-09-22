from django.shortcuts import render



def home(request):
    return render(request, 'home.html');

def bienvenido(request):
    return render(request, 'bienvenido.html');

def contactenos(request):
    return render(request, 'contactenos.html');

def registro(request):
    return render(request, 'registro.html');

def servicios(request):
    return render(request, 'servicios/servicios.html');
