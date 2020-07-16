from django import forms 
from django.utils.translation import gettext_lazy as _
from inventario.models import Proveedor, Producto

class ProveedorForm(ModelForm):
	class Meta:
		model = Proveedor
		fields = ('nombre', 'telefono', 'direccion')

class ArticuloForm(ModelForm):
	class Meta:
		model = Producto
		fields = ('nombre', 'descripcion', 'precioventa', 'preciocompra','existencia','promocion','fkproveedor','fkcategoria')
        labels = {
			'nombre': _('Nombre'),
			'descripcion': _('Descripción'),
			"precioventa":"Precio de Venta",
			"existencia":"Precio de Compra",
			"promocion":"Existencia",
            "fkproveedor":"Promoción",
        }
