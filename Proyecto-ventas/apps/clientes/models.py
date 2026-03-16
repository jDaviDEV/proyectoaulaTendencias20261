from django.db import models
 
class Cliente(models.Model):
    nombre = models.CharField("Nombre",max_length=100)
    apellido = models.CharField("Apellido",max_length=100)
    cedula = models.CharField("Cedula",max_length=20, unique=True)
    edad = models.IntegerField("Edad")
    telefono = models.CharField("Teléfono",max_length=15)
    direccion = models.CharField("Dirección",max_length=200)
    email = models.EmailField("Email")
 
    def __str__(self):
        return f'{self.nombre} {self.apellido}'