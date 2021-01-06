from django.db import models
from phone_field import PhoneField
from apps.inventario.models import *
# Create your models here.

class Pedido(models.Model):
    exito= models.BooleanField(default=False)
    cancelado = models.BooleanField(default=False)
    pendiente = models.BooleanField(default=True)
    subtotal =models.DecimalField(max_digits=5,decimal_places=2,default=0)
    display = models.BooleanField(default=False)
    fechaPedido = models.DateTimeField(auto_now=True)
    fkProveedor=models.ForeignKey(Proveedor,on_delete=models.CASCADE,null=True)
    comentario = models.CharField(max_length=60,blank=True)
    def agregarSubtotal(self,valor):
        self.subtotal=self.subtotal + valor
    def quitarSubtotal(self,valor):
        self.subtotal=self.subtotal - valor
    def setDisplay(self):
        self.display=True
    def setComentario(self,valor):
        self.comentarios=valor

class detalle_Pedido(models.Model):
    fkPedido = models.ForeignKey(Pedido, on_delete=models.CASCADE,null=True)
    cantidad = models.IntegerField(default=1)
    fkProducto =models.ForeignKey(Producto, on_delete=models.CASCADE,null=True)
    subtotal = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    comentario = models.CharField(max_length=60,blank=True)
    def setfkPedido(self,valor):
        self.fkPedido=valor
    def setfkProducto(self,valor):
        self.fkProducto=valor
    def setCantidad(self,valor):
        self.cantidad=valor
    def setComentario(self, valor):
        self.comentario=valor
    def setSubtotal(self):
        self.subtotal=self.cantidad*self.fkProducto.preciocompra
    def getSubtotal(self):
        return self.subtotal


class Tipo_Pago(models.Model):
    tipo = models.CharField(max_length=60)
    detalle = models.CharField(max_length=60)
    def __str__(self):
        return '%s'%(self.tipo)

class Pago(models.Model):
    fk_Tipo_Pago=models.ForeignKey(Tipo_Pago,on_delete=models.CASCADE,null=True)
    fecha =models.DateField(null=False)
    fk_pedido=models.ForeignKey(Pedido,on_delete=models.CASCADE,null=True)
    def setfk_Pedido(self,valor):
        self.fk_pedido=valor
    def set_fk_Tipo(self,valor):
        self.fk_Tipo_Pago=valor
    def setFecha(self, valor):
        self.fecha=valor
    def __str__(self):
        return '%s'%(self.fecha)
