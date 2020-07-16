from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from random import randrange, choice
#librerias usadas para articulo y proveedor
from .forms	import *
from django.views.generic import *
from apps.inventario.models import Proveedor, Producto
from apps.compras.models import *
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
# Create your views here.
#falta agregar verificación por rol
@login_required
def indexCompras(request):
	return render(request,'compras/index.html')

def proveedor_list(request):
	proveedors = Proveedor.objects.all()
	return render(request,'compras/proveedor/proveedor_list.html',{'proveedors':proveedors})
def save_proveedor_form(request, form, template_name):
	data = dict()
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			data['form_is_valid']=True
			proveedors = Proveedor.objects.all()
			data['html_proveedor_list'] = render_to_string('compras/proveedor/proveedor_list_2.html',
				{'proveedors':proveedors})
		else:
			data['form_is_valid']=False
	context = {'form':form}
	data['html_form'] = render_to_string(
		template_name,
		context,
		request = request,
	)
	return JsonResponse(data)
def proveedor_create(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
    else:
        form = ProveedorForm()
    return save_proveedor_form(request, form, 'compras/proveedor/proveedor_create.html')
def proveedor_update(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
    else:
        form = ProveedorForm(instance=proveedor)
    return save_proveedor_form(request, form, 'compras/proveedor/proveedor_update.html')
def proveedor_delete(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    data = dict()
    if request.method == 'POST':
        proveedor.delete()
        data['form_is_valid'] = True  
        proveedors = Proveedor.objects.all()
        data['html_proveedor_list'] = render_to_string('compras/proveedor/proveedor_list_2.html', {
            'proveedors': proveedors
        })
    else:
        context = {'proveedor': proveedor}
        data['html_form'] = render_to_string('compras/proveedor/proveedor_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)


def articulo_list(request):
	articulos = Producto.objects.all()
	return render(request,'compras/articulo/articulo_list.html',{'articulos':articulos})
def save_articulo_form(request, form, template_name):
	data = dict()
	if request.method == 'POST':
		#form = ArticuloForm(request.POST)
		if form.is_valid():
			form.save()
			data['form_is_valid']=True
			articulos = Producto.objects.all()
			data['html_articulo_list'] = render_to_string('compras/articulo/articulo_list_2.html',
				{'articulos':articulos})
		else:
			data['form_is_valid']=False
	context = {'form':form}
	data['html_form'] = render_to_string(
		template_name,
		context,
		request = request,
	)
	return JsonResponse(data)
def articulo_create(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
    else:
        form = ArticuloForm()
    return save_articulo_form(request, form, 'compras/articulo/articulo_create.html')
def articulo_update(request, pk):
    articulo = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ArticuloForm(request.POST, instance=articulo)
    else:
        form = ArticuloForm(instance=articulo)
    return save_articulo_form(request, form, 'compras/articulo/articulo_update.html')
def articulo_delete(request, pk):
    articulo = get_object_or_404(Producto, pk=pk)
    data = dict()
    if request.method == 'POST':
        articulo.delete()
        data['form_is_valid'] = True  
        articulos = Producto.objects.all()
        data['html_articulo_list'] = render_to_string('compras/articulo/articulo_list_2.html', {
            'articulos': articulos
        })
    else:
        context = {'articulo': articulo}
        data['html_form'] = render_to_string('compras/articulo/articulo_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)


def verpedidos(request):
	proveedor = Proveedor.objects.all()
	producto = Producto.objects.all()
	contexto = {'proveedores':proveedor,'productos':producto}
	return render(request, 'compras/pedidos/gestionar_pedidos.html',contexto)


def crearPedido(request):'''en esta crea el pedido vacío, se ejecutaría cuando den click al botón correspondiente a "crear pedido" (genera una url asignando esta vista)
                        luego envialo a otra pantalla con un formulario sencillo para elegir el proveedor y en la vista que procese el formulario buscas el proveedor con 
                        el código que mandes desde este y asignas proveedor  y pago; luego está página te envía a la de agregar productos (lines de pedido)
                        que imprimirias una tabla con un boton de agregar al final y envias el código del pedido y del producto, e incluso las cantidades podés asignarlas 
                        como en wichos, con una pantalla emergente
                        '''



def agregarPedido(request):
    if request.method=='POST':
        form = pedidoForm(request.POST)
        if  form.is_valid():
            #ped = Pedido()
            ped.save()
            Lin=detalle_Pedido()
            #Lin.setfkProducto(Producto.objects.get(id=form.producto.id))
            Lin.setfkPedido(Pedido.objects.get(id=ped.id))

            ped = Pedido.objects.get(id=ped.id)
            ped.setComentario('form.comentario')
            ped.setDisplay()
            ped.save()
            ped = Pedido.objects.get(id=ped.id)
            ped.subtotal = ped.subtotal + Lin.getSubtotal()
            Lin.setSubtotal()
            Lin.save()
            ped.save()
        return redirect('compras:reCom')
    else:
        proveedor = Proveedor.objects.all()
        producto = Producto.objects.all()
        pedido = Pedido.objects.all().filter(display=True)
        form=pedidoForm ()
        contexto={'form':form,'proveedores':proveedor,'productos':producto,'pedidos':pedido}
        return render(request,'compras/pedidos/generar_pedidos.html',contexto)

class PedidosList(ListView):
    model = detalle_Pedido
    template_name = 'compras/pedidos/gestionar_pedidos.html'

class PedidosCreate(CreateView):
    model = detalle_Pedido
    form_class = pedidoForm
    template_name = 'compras/pedidos/generar_pedidos.html'
    success_url = reverse_lazy('compras:reCom')