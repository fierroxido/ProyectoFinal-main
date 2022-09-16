from asyncio.windows_events import NULL
from multiprocessing import context
from django.shortcuts import render
from .models import Carrito, Servicio

# Create your views here.
def verProductos(request, id=NULL):

    if not id:
        listaServicios= Servicio.objects.all()
        context={
            'servicios':listaServicios,
        }
        return render(request,'servicios/servicios.html', context)
    else:
        id=int(id)
        regServicio= Servicio.objects.get(id=id)
        context={
            'servicio': regServicio,
        }
        return render(request,'servicios/unServicios.html', context)


def agregar (request, id=NULL):
    id= int(id)
    user= request.user
    existe= Carrito.objects.filter(servicio= regServicio, estado='carrito').exists()

    if existe:
        regCarrito= Carrito.objects.get(servicio= regServicio, estado='carrito')
        regCarrito.cantidad +=1
        regCarrito.save()
    else:
        regCarrito= Carrito()