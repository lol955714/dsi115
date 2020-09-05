from django.db import models
from apps.inventario.models import *
from django.conf import settings
# Create your models here.

#class tipoPago(models.Model):


class pedido(models.Model):
	vendedor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE )
	cliente = models.CharField(max_length=50)
	total = models.DecimalField(max_digits=6,decimal_places=2)
	#tipoPago = models.foreignKey(tipoPago, on_delete=models.CASCADE)

class lineaDeVenta(models.Model):
	articulofk = models.ForeignKey(Producto, on_delete=models.CASCADE)
	pedidofk = models.ForeignKey(pedido, on_delete=models.CASCADE)
	cantidad = models.IntegerField(default=1)
	subtotal = models.DecimalField(max_digits=6,decimal_places=2,default=0)

class Empleado(models.Model):
	nombres = models.CharField(max_length=40,null=False)
	apellidos = models.CharField(max_length=40,null=False)
	telefono= models.CharField(max_length=8,null=False,unique=True)
	dui = models.CharField(max_length=9,null=False,unique=True)
	nit = models.CharField(max_length=14,null=False,unique=True)
	def __str__(self):
		return '%s'%(self.nombres)