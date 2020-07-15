from django.db import models
from phone_field import PhoneField
# Create your models here.

class Proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40,blank=False)
    direccion = models.TextField(max_length=60,blank=True)
    mobile = PhoneField(unique=True, blank=True, help_text='Agregar numero telefonico')
    email = models.EmailField(max_length=254)
    

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    proveedor = models.ForeignKey(
        Proveedor,
        on_delete=models.CASCADE,
    )
    nombre = models.CharField(max_length=40,blank=False)
    precioCompra = models.DecimalField(max_digits=5, decimal_places=2,blank=True, default=0)
    precioVenta = models.DecimalField(max_digits=5, decimal_places=2,null=False)
    existencia = models.PositiveIntegerField(null=True, blank=True)
    descripcion = models.TextField(max_length=60,blank=True)

    def __str__(self):
        return self.nombre