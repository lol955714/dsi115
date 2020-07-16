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

class Pedido(models.Model):
    exito= models.BooleanField(default=False)
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




