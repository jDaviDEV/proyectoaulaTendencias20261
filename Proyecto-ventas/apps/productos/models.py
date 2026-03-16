# Create your models here.
from django.db import models
 
class Producto(models.Model):
    nombre_producto = models.CharField('Producto', max_length=150)
    precio = models.DecimalField('Precio', max_digits=10, decimal_places=2)
    stock = models.IntegerField()
 
    def __str__(self):
        return self.nombre_producto