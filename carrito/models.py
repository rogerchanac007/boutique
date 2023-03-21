from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to='imagenes/')

    def __str__(self):
        return self.nombre

