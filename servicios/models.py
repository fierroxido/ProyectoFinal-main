
from django.db import models

from accounts.models import Account

# Create your models here.

class Servicio(models.Model):
    nombre= models.CharField(max_length=100, null=False)
    descripcion= models.CharField(max_length=300, null=True)
    precio= models.DecimalField(max_digits=8, decimal_places=2)
    imagen= models.ImageField(upload_to='servicios')
    icono= models.ImageField(upload_to='iconos')

    def __str__(self):
        return self.nombre


class Carrito(models.Model):
    ESTADOS=(
        ('carrito','carrito'),
        ('cancelado','cancelado'),
        ('comprado','comprado'),
    )
    cliente= models.ForeignKey(Account, on_delete=models.CASCADE, null=False)
    servicio= models.ForeignKey(Servicio, on_delete=models.CASCADE, null=False)
    precio= models.DecimalField(max_digits=8, decimal_places=2)
    #cantidad= models.IntegerField(default=1, null=False)
    estado=models.CharField(max_length=15, choices=ESTADOS, default='carrito')
    fecha= models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.cliente