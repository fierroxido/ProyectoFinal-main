from django.urls import path
from . import views

urlpatterns =[
    path('servicio/', views.verServicios, name="servicios"),
    path('servicio/<str:id>', views.verServicios, name="servicio"),
    path('servicio/<str:id>', views.agregar, name="carrito"),
]