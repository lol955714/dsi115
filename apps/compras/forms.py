from django import forms 
from apps.inventario.models import Proveedor, Producto

class ProveedorForm(forms.ModelForm):
	class Meta:
		model = Proveedor
		fields = ('nombre', 'telefono', 'direccion')

class ArticuloForm(forms.ModelForm):
	class Meta:
		model = Producto
		fields = ('nombre', 'descripcion', 'precioventa', 'preciocompra','promocion','fkproveedor')

