from django import forms 
from django.forms import widgets
from apps.ventas.models import *
from apps.compras.models import Tipo_Pago
from django.conf import settings

tipos=Tipo_Pago.objects.all()

class EmpleadoForm(forms.ModelForm):
	class Meta:
		model = Empleado
		fields = [
			'clave', 
			'nombres', 
			'apellidos', 
			'telefono', 
			'dui',
			'nit',
		]
		labels={
			'clave':'Clave del Empleado',
			'nombres':'Nombres del Empleado',
			'apellidos':'Apellidos del Empleado',
			'telefono':'# Telefonico',
			'dui':'DUI',
			'nit':'NIT',
		}
		widgets={
			'clave' : forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'Introduzca la clave del nuevo empleado', 
			}),
			'nombres' : forms.TextInput(attrs={'class':'form-control'}),
			'apellidos' : forms.TextInput(attrs={'class':'form-control'}),
			'telefono' : forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'Introduzca numero telefonico', 
			}),
			'dui' : forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Introduzca el DUI del nuevo empleado', 
			}),
			'nit' : forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'Introduzca el NIT del nuevo empleado', 
				#'help_texts':'Ingrese el NIT completo',
			}),
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

class AsignacionForm(forms.ModelForm):
	class Meta:
		model = Asignacion
		fields = [
			'empleadofk',
			'meta_asignadafk',  
			'tipo_meta',
		]
		labels={
			'empleadofk':'Seleccione el empleado',
			'meta_asignadafk':'Asigne una meta',
			'tipo_meta':'Seleccione el tipo de meta',
		}
		widgets={
			'empleadofk' : forms.Select(attrs={'class':'form-control'}),
			'meta_asignadafk' : forms.Select(attrs={'class':'form-control'}),
			'tipo_meta': forms.Select(attrs={'class':'form-control'}),
		}

class iniciarVe(forms.Form):
	credito = forms.BooleanField(label="Necesitará crédito fiscal?",required=False)
	cliente = forms.CharField(label='Nombre del cliente',required=True,max_length=25)

class agregar(forms.Form):
	cantidad=forms.IntegerField(label="Cantidad de productos", required=True, min_value=1)

class contra(forms.Form):
	typ = forms.ModelMultipleChoiceField(tipos,required=True, label='Selecciones el método de pago')
	passwd = forms.CharField(widget=forms.PasswordInput, required=True,min_length=4,max_length=4)