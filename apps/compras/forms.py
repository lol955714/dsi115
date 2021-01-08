from django import forms 
from apps.inventario.models import *
from .models import *

#class ProveedorForm(forms.ModelForm):
#	class Meta:
#		model = Proveedor
#		fields = ('nombre', 'direccion', 'mobile', 'email',)

#class ArticuloForm(forms.ModelForm):
#	class Meta:
#		model = Producto
#		fields = ('nombre', 'precioCompra', 'proveedor', 'precioVenta','existencia','descripcion')

prove=Proveedor.objects.all()
tipos=Tipo_Pago.objects.all()

class comentarioPedido(forms.Form):
	comentario=forms.CharField(label="Nota especial",max_length=50,required=False)

class pedidoForm(forms.Form):
	proveedores=forms.ModelMultipleChoiceField(prove,required=True)
	tipo=forms.ModelMultipleChoiceField(tipos,required=True)
	
class formulario(forms.Form):
	cantidad=forms.IntegerField(required=True)
	comentario=forms.CharField(label="Nota especial",max_length=50,required=False)

class ProveedorForm(forms.ModelForm):
	class Meta:
		model = Proveedor
		fields = ('nombre', 'telefono', 'direccion','nombreRepresentante','telefonoPersonal')
		labels={
			'nombre':'Nombre del Proveedor',
			'telefono':'Telefono',
			'direccion':'Dirección',
			'nombreRepresentante':'Nombre del vendedor',
			'telefonoPersonal':'teléfono personal',
		}
		widgets={
			'nombre' : forms.TextInput(attrs={'class':'form-control'}),
			'telefono' : forms.TextInput(attrs={'class':'form-control'}),
			'direccion' : forms.TextInput(attrs={'class':'form-control'}),
			'nombreRepresentante' :   forms.TextInput(attrs={'class':'form-control'}),
			'telefonoPersonal' :   forms.TextInput(attrs={'class':'form-control'}),
		}

class ArticuloForm(forms.ModelForm):
	class Meta:
		model = Producto
		fields = [
			'nombre', 
			'descripcion', 
			'precioventa', 
			'preciocompra',
			'existencia',
			'promocion',
			'fkproveedor',
			'fkcategoria',
			'minimo',
		]
		labels={
			'nombre':'Nombre Articulo',
			'descripcion':'Descripción',
			'precioventa':'Precio de Venta',
			'preciocompra':'Precio de Compra',
			'existencia':'Existencia',
			'promocion':'Promocion',
			'fkproveedor':'Proveedor',
			'fkcategoria':'Categoria',
			'minimo':'cantidad mínima de producto',
		}
		widgets={
			'nombre' : forms.TextInput(attrs={'class':'form-control'}),
			'descripcion' : forms.TextInput(attrs={'class':'form-control'}),
			'precioventa' : forms.NumberInput(attrs={'class':'form-control'}),
			'preciocompra' : forms.NumberInput(attrs={'class':'form-control'}),
			'existencia' : forms.NumberInput(attrs={'class':'form-control'}),
			#'promocion' : forms.ChoiceField(attrs={'class':'form-control'}),
			'fkproveedor' : forms.Select(attrs={'class':'form-control'}),
			'fkcategoria' : forms.Select(attrs={'class':'form-control'}),
			'minimo' : forms.NumberInput(attrs={'class':'form-control'}),
		}


'''
class pedidoForm(forms.ModelForm):

	#def __init__(self, request,*args,**kwargs):
	#	super(pedidoForm,self).__init__(*args,**kwargs)
	#	self.fields['proveedor'].queryset = (detalle_Pedido.fkProducto).objects.filter(fkProducto=Producto.id)

	class Meta:
		model = detalle_Pedido
		fields=[
			'fkProducto',
			'fkPedido',
			'cantidad',
		#	'comentario',
		]
		labels={
			'fkProducto':'Producto',
			'fkProovedor':'Proovedor',
			'cantidad':'Cantidad',
		#	'comentario':'Comentario',
		}
		widgets={
			#'fkProducto' : forms.ChoiceField(attrs={'class':'form-control'}),
			#'fkProovedor' : forms.Select(),
			#'cantidad' : forms.IntegerField(),
		#	'comentario' : forms.CharField(),
		}
'''