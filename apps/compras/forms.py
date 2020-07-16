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

class pedidoForm(forms.Form):
	proveedores=forms.ModelMultipleChoiceField(prove,required=True)
	tipo=forms.ModelMultipleChoiceField(tipos,required=True)



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