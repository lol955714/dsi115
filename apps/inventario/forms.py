from apps.inventario.models import *
from django import forms

from django.forms import widgets
from django.forms import fields, CheckboxInput

class productoForm(forms.ModelForm):
	fkcate = forms.ModelChoiceField(queryset=CategoriaIncidencia.objects.all())
	comentario = forms.CharField(required=False, max_length=150)
	class Meta:
		model=Producto
		fields=[
			'nombre',
			'descripcion',
			'precioventa',
			'preciocompra',
			'existencia',
			'promocion',
			'fkcategoria',
			'fkproveedor',
			]
		labels={

			'nombre':'Nombre',
			'descripcion':'Descripcion:',
			'precioventa':'Precio de Venta:',
			'preciocompra':'Precio de Compra:',
			'existencia':'Existencias:',
			'promocion':'Promocion:',
			'fkcategoria':'Categoria',
			'fkproveedor':'Proveedor',
		}
		widgets={
			'nombre': forms.TextInput(),
			'descripcion': forms.TextInput(),
			'precioventa': forms.NumberInput(),
			'preciocompra': forms.NumberInput(),
			'existencia': forms.TextInput(),
			'promocion': forms.CheckboxInput(),
			'fkproveedor': forms.Select(),
			'fkcategoria': forms.Select(),
		}


class elimiarForm(forms.Form):
	confirmar = forms.CheckboxInput()

class cuentaForm(forms.ModelForm):
	class Meta:
		model=Cuenta
		fields=[
			'titulo',
			'monto',
			'fechalimite',
			'comentario',
			'cobrar',
			]
		labels={

			'titulo':'Titulo',
			'monto':'Monto:',
			'fechalimite':'Fecha limite:',
			'comentario':'Comentario:',
			'cobrar':'Marque la casilla si es una cuenta por cobrar, o dejela en blanco si es por pagar.',
		}
		widgets={
			'titulo': forms.TextInput(),
			'monto': forms.TextInput(),
			'fechalimite': forms.DateTimeInput(),
			'comentario': forms.TextInput(),
			'cobrar': forms.CheckboxInput(),
		}