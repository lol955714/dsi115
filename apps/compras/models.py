from django.db import models
from phone_field import PhoneField
from apps.inventario.models import *
# Create your models here.

class Pedido(models.Model):
    exito= models.BooleanField(default=False)
    fkProveedor=models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    cancelado = models.BooleanField(default=False)
    pendiente = models.BooleanField(default=True)
    subtotal = models.FloatField(null=True,default=0)
    display = models.BooleanField(default=False)
    fechaPedido = models.DateTimeField(auto_now=True)
    def setDisplay(self):
        self.display=True
    def setComentario(self,valor):
        self.comentarios=valor

class detalle_Pedido(models.Model):
    fkPedido = models.ForeignKey(Pedido, on_delete=models.CASCADE,null=True)
    cantidad = models.IntegerField(default=1)
    fkProducto =models.ForeignKey(Producto, on_delete=models.CASCADE,null=True)
    subtotal = models.FloatField(null=True,default=0)
    comentario = models.CharField(max_length=60,blank=True)
    def setfkPedido(self,valor):
        self.fkPedido=valor
    def setfkProducto(self,valor):
        self.fkProducto=valor
    def setCantidad(self,valor):
        self.cantidad=valor
    def setSubtotal(self):
        self.subtotal=self.cantidad*self.fkProducto.precioCompra
    def getSubtotal(self):
        return self.subtotal


class Tipo_Pago(models.Model):
    tipo = models.CharField(max_length=60)
    detalle = models.CharField(max_length=60)

class Pago(models.Model):
    fk_Tipo_Pago=models.ForeignKey(Tipo_Pago,on_delete=models.CASCADE,null=False)
    fecha =models.DateField(null=False)
    fk_pedido=models.ForeignKey(Pedido,on_delete=models.CASCADE)

