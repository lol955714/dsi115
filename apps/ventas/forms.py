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
			'telefono' : forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'Introduzca numero telefonico', 
				'minlength':'8',
                'maxlength':'8',
			}),
			'dui' : forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'Introduzca el DUI del nuevo empleado', 
				'minlength':'9',
                'maxlength':'9',
			}),
			'nit' : forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'Introduzca el NIT del nuevo empleado', 
				#'help_texts':'Ingrese el NIT completo',
				'minlength':'14',
                'maxlength':'14',
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
		]
		labels={
			'empleadofk':'Seleccione el empleado',
			'meta_asignadafk':'Asigne una meta',
		}
		widgets={
			'empleadofk' : forms.Select(attrs={'class':'form-control'}),
			'meta_asignadafk' : forms.Select(attrs={'class':'form-control'}),
		}

class iniciarVe(forms.Form):
	vendedor = forms.ModelMultipleChoiceField(vendedores,required=True,label="vendedor")
	cliente = forms.CharField(label='Nombre del cliente',required=True,max_length=25)

class agregar(forms.Form):
	cantidad=forms.IntegerField(label="Cantidad de productos", required=True, min_value=1)