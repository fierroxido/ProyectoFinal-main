from django.db import models

# Create your models here.

class Servicio(models.Model):
    nombre= models.CharField(max_length=100, null=False)
    descripcion= models.CharField(max_length=300, null=True)
    precio= models.DecimalField(max_digits=8, decimal_places=2)
    imagen= models.ImageField(upload_to='servicios')
    icono= models.ImageField(upload_to='iconos')

def __str__(self):
    return self.nombre