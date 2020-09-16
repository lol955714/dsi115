from django import forms 
from django.forms import widgets
from apps.ventas.models import *
from django.conf import settings

vendedores= Empleado.objects.all()

class EmpleadoForm(forms.ModelForm):
	class Meta:
		model = Empleado
		fields = [
			'nombres', 
			'apellidos', 
			'telefono', 
			'dui',
			'nit',
		]
		labels={
			'nombres':'Nombres del Empleado',
			'apellidos':'Apellidos del Empleado',
			'telefono':'# Telefonico',
			'dui':'DUI',
			'nit':'NIT',

		}
		widgets={
			'nombres' : forms.TextInput(attrs={'class':'form-control'}),
			'apellidos' : forms.TextInput(attrs={'class':'form-control'}),
			'telefono' : forms.TextInput(attrs={'class':'form-control'}),
			'dui' : forms.NumberInput(attrs={'class':'form-control'}),
			'nit' : forms.NumberInput(attrs={'class':'form-control'}),
		}

class MetaForm(forms.ModelForm):
	class Meta:
		model = Metas
		fields = [

			'monto_asignado', 
			'descripcion', 
		]
		labels={

			'monto_asignado':'Ingrese el monto en $',
			'descripcion':'Descripcion de la meta',
		}
		widgets={

			'monto_asignado' : forms.NumberInput(attrs={'class':'form-control'}),
			'descripcion' : forms.TextInput(attrs={'class':'form-control'}),

		}

class iniciarVe(forms.Form):
	vendedor = forms.ModelMultipleChoiceField(vendedores,required=False,label="vendedor")
	cliente = forms.CharField(label='Nombre del cliente',required=True,max_length=25)
