from django import forms 
from apps.ventas.models import *

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
