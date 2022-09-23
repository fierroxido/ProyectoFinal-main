from django.contrib import admin

from .models import Servicio, Carrito

# Register your models here.
class CarritoAdmin(admin.ModelAdmin):
    list_display= ('id', '__str__')

admin.site.register(Carrito, CarritoAdmin)

class ServicioAdmin(admin.ModelAdmin):
    list_display= ('id', '__str__')

admin.site.register(Servicio,ServicioAdmin)