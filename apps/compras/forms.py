from django import forms 
from django.utils.translation import gettext_lazy as _
from apps.inventario.models import Proveedor, Producto

class ProveedorForm(forms.ModelForm):
	class Meta:
		model = Proveedor
		fields = ('nombre', 'telefono', 'direccion')
		labels = {
			'nombre': _('Nombre'),
			'telefono': _('Número Telefonico'),
			'direccion': _('Dirección'),
        }
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'telefono': forms.TextInput(attrs={'class':'form-control'}),
			'direccion': forms.TextInput(attrs={'class':'form-control'}),
		} 

class ArticuloForm(forms.ModelForm):
	class Meta:
		model = Producto
		fields = ('nombre', 'descripcion', 'precioventa', 'preciocompra','existencia','promocion','fkproveedor','fkcategoria')
		labels = {
			'nombre': _('Nombre'),
			'descripcion': _('Descripción'),
			'precioventa': _('Precio de Venta'),
			'preciocompra': _('Precio de Compra'),
			'existencia': _('Existencia'),
			'promocion': _('Promocion'),
            'fkproveedor': _('Proveedor'),
			'fkcategoria': _('Categoria'),
        }
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'descripcion': forms.TextInput(attrs={'class':'form-control'}),
			'precioventa': forms.NumberInput(attrs={'class':'form-control'}),
			'preciocompra': forms.NumberInput(attrs={'class':'form-control'}),
			'existencia': forms.TextInput(attrs={'class':'form-control'}),
			#'promocion': forms.CheckboxInput(attrs={'class':'form-control'}),
			'fkproveedor': forms.Select(attrs={'class':'form-control'}),
			'fkcategoria': forms.Select(attrs={'class':'form-control'}),
		} 