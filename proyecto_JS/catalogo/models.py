from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    cantidad_en_stock = models.IntegerField()
    
    def __str__(self):
        return self.nombre + ' - ' + self.descripcion

