from django.db import models
from decimal import *

# Create your models here.
class Categoria(models.Model):
	nombre =models.CharField(max_length=30,null=False)
	descripcion =models.CharField(max_length=50,null=False)
	def __str__(self):
		return '%s'%(self.nombre)

class Proveedor(models.Model):
	nombre =models.CharField(max_length=30,null=True)
	nombreRepresentante=models.CharField(max_length=35,null=False)
	telefonoPersonal=models.CharField(max_length=8,null=False)
	telefono=models.CharField(max_length=8,null=False)
	direccion=models.CharField(max_length=150,null=False)
	estado =models.BooleanField(default=True,null=False)
	def __str__(self):
		return '%s'%(self.nombre)

class CategoriaIncidencia(models.Model):
	nombre = models.CharField(max_length=30, null=False)
	descripcion = models.CharField(max_length=150, null=False)
	def gePkCatInc(self):
		return self.id
	def __str__(self):
		return '%s'%(self.nombre)



class Producto(models.Model):
	nombre =models.CharField(max_length=30,null=False)
	descripcion =models.CharField(max_length=50,null=False,default='')
	precioventa =models.DecimalField(max_digits=5,decimal_places=2,null=False)
	preciocompra =models.DecimalField(max_digits=5,decimal_places=2,null=False)
	existencia =models.IntegerField(null=False)
	promocion =models.BooleanField(default=False)
	minimo=models.IntegerField(null=False)
	fkcategoria = models.ForeignKey(Categoria,on_delete=models.CASCADE,null=False)
	fkproveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE,null=False)
	def __str__(self):
		return '%s'%(self.nombre)
	def setNombre(self, valor):
		self.nombre = valor
	def setDescripcion(self, valor):
		self.descripcion = valor
	def setPrecioVenta(self, valor):
		self.precioventa = valor
	def setPrecioCompra(self, valor):
		self.preciocompra = valor
	def setExistencia(self, valor):
		self.existencia = valor
	def setFkCategoria(self, valor):
		self.fkcategoria = valor
	def setFkProveedor(self, valor):
		self.fkproveedor = valor
	def setFkIncidencia(self, valor):
		self.fkIncidencia = valor
	def agregarInventario(self, valor):
		self.existencia=self.existencia+valor
	def removerInventario(self, valor):
		self.existencia=self.existencia-valor

class Incidencia(models.Model):
	fkCategoriaIncidencia = models.ForeignKey(CategoriaIncidencia, on_delete=models.CASCADE, null=False, blank=False)
	fecha = models.DateTimeField(auto_now=True)
	descripcion = models.CharField(max_length=150, null=False)
	fkProducto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True, blank=True)
	def setCategoriaIncidencia(self, valor):
		self.fkCategoriaIncidencia = valor
	def setProducto(self, valor):
		self.fkProducto = valor
	def setDescripcion(self, valor):
		self.descripcion = valor

class Notificacion(models.Model):
	fecha = models.DateTimeField(auto_now=True)
	descripcion = models.CharField(max_length=150, null=False)

class Cuenta(models.Model):
	fechacreacion = models.DateTimeField(auto_now=True)
	comentario = models.CharField(max_length=150, null=False)
	titulo = models.CharField(max_length=150, null=True)
	monto= models.DecimalField(max_digits=5, decimal_places=2, null=False)
	cobrar = models.BooleanField(default=False) #True=Cobrar, False=Pagar
	archivada = models.BooleanField(default=False)
	fechalimite = models.CharField(max_length=150, null=True)