from django.db import models
from decimal import *

# Create your models here.
class Categoria(models.Model):
	nombre =models.CharField(max_length=30,null=False)
	descripcion =models.CharField(max_length=50,null=False)
	def __str__(self):
		return '%s'%(self.nombre)

class Proveedor(models.Model):
	nombre =models.CharField(max_length=30,null=False)
	telefono=models.CharField(max_length=8,null=False)
	direccion=models.CharField(max_length=150,null=False)
	estado =models.BooleanField(default=True,null=False)
	def __str__(self):
		return '%s'%(self.nombre)

class Producto(models.Model):
	nombre =models.CharField(max_length=30,null=False)
	precioventa =models.DecimalField(max_digits=5,decimal_places=2,null=False)
	preciocompra =models.DecimalField(max_digits=5,decimal_places=2,null=False)
	existencia =models.IntegerField(null=False)
	promocion =models.BooleanField(default=False)
	fkcategoria = models.ForeignKey(Categoria,on_delete=models.CASCADE,null=False)
	fkproveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE,null=False)
	def __str__(self):
		return '%s'%(self.nombre)

