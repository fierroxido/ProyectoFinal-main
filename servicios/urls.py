from django.urls import path
from . import views

urlpatterns =[
    path('servicio/', views.verServicios, name="servicios"),
    path('servicio/<str:id>', views.verServicios, name="servicio"),
    path('agregarcarrito/<str:id>', views.agregarCarrito, name="agregarCarrito"),
    path('vercarrito/', views.verCarrito, name="verCarrito"),
    path('eliminar/<str:id>', views.eliminarCarritoItem, name="eliminar"),
    path('citas/', views.citas, name="citas")
]