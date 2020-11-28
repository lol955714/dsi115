from django.db import models
from apps.inventario.models import *
from apps.compras.models import Tipo_Pago
from django.conf import settings
from django.core.validators import RegexValidator
import datetime
from django.utils.translation import gettext as _
from django.db.models import UniqueConstraint
# Create your models here.



class Metas(models.Model):
	monto_asignado = models.DecimalField(max_digits=6, decimal_places=2)
	descripcion = models.CharField(max_length=50)

	def __str__(self):
		return '%s'%(self.monto_asignado)

class Empleado(models.Model):
	clave= models.CharField(max_length=4,null=False,unique=True,validators=[
		RegexValidator(regex='^.{4}$', 
		message='El # ingresado es invalido, Debe tener 4 caracteres', 
		code='nomatch'
		)])
	nombres = models.CharField(max_length=40,null=False)
	apellidos = models.CharField(max_length=40,null=False)
	telefono= models.CharField(max_length=8,null=False,unique=True,validators=[
		RegexValidator(regex='^.{8}$', 
		message='El # ingresado es invalido, Debe tener 9 caracteres', 
		code='nomatch'
		)])
	dui = models.CharField(max_length=9,null=False,unique=True,validators=[
		RegexValidator(regex='^.{9}$', 
		message='El DUI ingresado es invalido, Debe tener 9 caracteres', 
		code='nomatch'
		)])
	nit = models.CharField(max_length=14,null=False,unique=True,validators=[
		RegexValidator(regex='^.{14}$', 
		message='El NIT ingresado es invalido, Debe tener 14 caracteres', 
		code='nomatch'
		)])
	def __str__(self):
		return '%s'%(self.nombres)

class Asignacion(models.Model):
	meta_asignadafk = models.ForeignKey(Metas, on_delete=models.CASCADE,null=False)	
	empleadofk = models.ForeignKey(Empleado, on_delete=models.CASCADE,null=False)
	fecha_asignacion = models.DateField(auto_now=True)
	monto_logrado = models.DecimalField(max_digits=6, decimal_places=2, blank=True, default=0)

	STATUS = (
      (1,  _('Diaria')),
      (2, _('Quincenal')),
      (3, _('Mensual')),
   )
	tipo_meta = models.PositiveSmallIntegerField(
      choices=STATUS,
      default=1,
   )
    
	#class Meta:
	#	UniqueConstraint(fields=['empleadofk', 'fecha_asignacion'], name='unique_booking')


class pedido(models.Model):
	nope = models.BooleanField(default=False)
	finalizada =models.BooleanField(default=False)
	fechaCreada =models.DateField(auto_now=True)
	vendedor = models.ForeignKey(Empleado, on_delete=models.CASCADE,null=True)
	cliente = models.CharField(max_length=50,null=True)
	total = models.DecimalField(max_digits=8,decimal_places=2,default=0)
	#errorContra =models.BooleanField(default=False)
	tipoPago = models.ForeignKey(Tipo_Pago, on_delete=models.CASCADE,null=True)
	def setVendedor(self, valor):
		self.vendedor=valor
	def setCliente(self, valor):
		self.cliente=valor
	def setTotal(self, valor):
		self.total=self.total + valor
	def setFinal(self):
		self.finalizada=True
	def quitar(self, valor):
		self.total=self.total-valor
	def setTipoPago(self, valor):
		self.tipoPago=valor
	def errorContra(self):
		if self.nope == True:
			self.nope = False
		else:
			self.error = True

class lineaDeVenta(models.Model):
	articulofk = models.ForeignKey(Producto, on_delete=models.CASCADE)
	pedidofk = models.ForeignKey(pedido, on_delete=models.CASCADE)
	cantidad = models.IntegerField(default=1)
	subtotal = models.DecimalField(max_digits=6,decimal_places=2,default=0)
	def setArticulo(self, valor):
		self.articulofk=valor
	def setPedido(self, valor):
		self.pedidofk=valor
	def setCantidad(self, valor):
		self.cantidad=valor
	def sub(self):
		self.subtotal=self.cantidad * self.articulofk.precioventa
	def getSubtotal(self):
		return self.subtotal

