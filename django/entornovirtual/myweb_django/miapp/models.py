from django.db import models

# Create your models here.


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    modelo = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    fecha_creacion = models.DateField(auto_now_add=True)


class Articulo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    fecha_creacion = models.DateField(auto_now_add=True)
