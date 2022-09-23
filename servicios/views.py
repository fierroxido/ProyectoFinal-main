from asyncio.windows_events import NULL
from multiprocessing import context
from django.shortcuts import render
from .models import Carrito, Servicio

# Create your views here.
def verServicios(request, id=NULL):

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
        
        return render(request,'servicios/unServicio.html', context)


def agregarCarrito(request, id):
    id= int(id)
    user= request.user
    regServicio=Servicio.objects.get(id=id)
    existe= Carrito.objects.filter(cliente=user, servicio= regServicio, estado='carrito').exists()
    print('-----------------------')
    print(existe)
    context={}
    if existe:
        context['aviso']= 'El servicio ya fue agregado al carrito'
    else:
        regCarrito= Carrito(cliente=user, servicio= regServicio, precio= regServicio.precio)
        regCarrito.save()

    listaServicios = Servicio.objects.all()
    context[ 'servicios']= listaServicios

    return render(request, 'servicios/carrito.html', context)



def verCarrito(request):
    regUser = request.user
    carrito = Carrito.objects.filter(cliente=regUser, estado='carrito')
    # Recorrer elementos del carrito para calcular totales
   
    listaCarrito = []
    total = 0
    for ser in carrito:
        unServicio={
			'cantidad': ser.cantidad,
			'icono': ser.servicio.icono,
			'nombre': ser.servicio.nombre,
			'valor': ser.servicio.precio,
			
			'total': int(ser.cantidad)	* int(ser.servicio.precio),
			'id': ser.id,
	    }
 
        listaCarrito.append(unServicio) 
        total += unServicio['total']

    #ensamblar datos para la plantilla
    context = {
        'carrito':  listaCarrito,
        'subtotal': total,
        'total': total ,
    }
 
    return render(request, 'servicios/carrito.html', context)

def eliminarCarritoItem(request, id):
    #regUser= request.user
    regCarrito= Carrito.objects.get(id=id)
    regCarrito.estado= 'cancelado'
    regCarrito.save()
    return verCarrito(request)