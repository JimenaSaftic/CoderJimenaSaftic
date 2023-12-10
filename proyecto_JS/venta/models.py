from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre_apellido= models.CharField(max_length=20)
    nro_cuit = models.IntegerField()
    email = models.EmailField()
    
    def __str__(self):
        return self.nombre_apellido + ", CUIT: " + str(self.nro_cuit)

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="venta")
    nro_factura = models.IntegerField()
    producto = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    
    def __str__(self):
        return "factura nro: " + str(self.nro_factura)