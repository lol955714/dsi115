from django import forms 
from .models import Proveedor, Producto

class ProveedorForm(forms.ModelForm):
	class Meta:
		model = Proveedor
		fields = ('nombre', 'direccion', 'mobile', 'email',)

class ArticuloForm(forms.ModelForm):
	class Meta:
		model = Producto
		fields = ('nombre', 'precioCompra', 'proveedor', 'precioVenta','existencia','descripcion')

