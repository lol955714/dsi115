from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from random import randrange, choice
#librerias usadas para articulo y proveedor
from .forms	import *
from datetime import date
from django.views.generic import *
from apps.inventario.models import Proveedor, Producto
from apps.compras.models import *
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from .forms import *
from django.template.loader import render_to_string
from django.urls import reverse_lazy
# Create your views here.
#falta agregar verificación por rol
@login_required
def indexCompras(request):
	return render(request,'compras/gestionar_pedidos.html')

@login_required
def proveedor_list(request):
	proveedors = Proveedor.objects.all()
	return render(request,'compras/proveedor/proveedor_list.html',{'proveedors':proveedors})

@login_required
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

@login_required
def proveedor_create(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
    else:
        form = ProveedorForm()
    return save_proveedor_form(request, form, 'compras/proveedor/proveedor_create.html')


@login_required
def proveedor_update(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
    else:
        form = ProveedorForm(instance=proveedor)
    return save_proveedor_form(request, form, 'compras/proveedor/proveedor_update.html')
    
@login_required
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

@login_required
def articulo_list(request):
	articulos = Producto.objects.all()
	return render(request,'compras/articulo/articulo_list.html',{'articulos':articulos})

@login_required
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

@login_required
def articulo_create(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
    else:
        form = ArticuloForm()
    return save_articulo_form(request, form, 'compras/articulo/articulo_create.html')

@login_required
def articulo_update(request, pk):
    articulo = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ArticuloForm(request.POST, instance=articulo)
    else:
        form = ArticuloForm(instance=articulo)
    return save_articulo_form(request, form, 'compras/articulo/articulo_update.html')
@login_required
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

@login_required
def verpedidos(request):
	pedidos=Pedido.objects.all()
	contexto = {'pedidos':pedidos}
	return render(request, 'compras/pedidos/gestionar_pedidos.html',contexto)


#def crearPedido(request):
@login_required
def lineapedido(request, idPedido, idProveedor):#muestra los productos dle proveedor y da pauta para añadir
    cat=Categoria.objects.get(id=idProveedor)
    produc=Producto.objects.all().filter(fkcategoria= cat)
    detalle=detalle_Pedido.objects.all().filter(fkPedido=Pedido.objects.get(id=idPedido))
    var=detalle.count()
    return render(request,'compras/pedidos/realizar_pedido.html',{'productos':produc,'idPedido':idPedido,'idProveedor':idProveedor,'detalle':detalle,'var':var})

@login_required
def cancelar(request, idPedido):
    pedido=Pedido.objects.get(id=idPedido)
    detalle=detalle_Pedido.objects.all().filter(fkPedido=pedido)
    detalle.delete()
    pedido.delete()
    return redirect('compras:index')

@login_required
def borrarLinea(request, idLinea, idPedido, producto, idProveedor):
    deta=detalle_Pedido.objects.get(id=int(idLinea))
    pedido=Pedido.objects.get(id=idPedido)
    pedido.quitarSubtotal(deta.getSubtotal())
    pedido.save()
    print(deta.getSubtotal())
   
    cat=Categoria.objects.get(id=idProveedor)
    produc=Producto.objects.all().filter(fkcategoria= cat)
    detalle=detalle_Pedido.objects.all().filter(fkPedido=Pedido.objects.get(id=idPedido))
    var=detalle.count()
    deta.delete()
    return render(request,'compras/pedidos/realizar_pedido.html',{'productos':produc,'idPedido':idPedido,'idProveedor':idProveedor,'detalle':detalle,'var':var})

@login_required
def editarLinea(request, idLinea, idPedido, producto, idProveedor):
    if request.method=='POST':
        fom=formulario(request.POST)
        if fom.is_valid():
            form_data=fom.cleaned_data
            deta=detalle_Pedido.objects.get(id=idLinea)
            deta.delete()
            detalle=detalle_Pedido()
            pedido=Pedido.objects.get(id=idPedido)
            producto=Producto.objects.get(id=producto)
            pedido.quitarSubtotal(detalle.getSubtotal())       
            detalle.setfkPedido(pedido)
            detalle.setfkProducto(producto)
            detalle.setCantidad(form_data.get("cantidad"))
            detalle.setSubtotal()
            pedido.agregarSubtotal(detalle.getSubtotal())
            detalle.setComentario(form_data.get("comentario"))
            detalle.save()
            pedido.save()
            cat=Categoria.objects.get(id=idProveedor)
            produc=Producto.objects.all().filter(fkcategoria= cat)
            detalle=detalle_Pedido.objects.all().filter(fkPedido=Pedido.objects.get(id=idPedido))
            var=detalle.count()
            print("holi")
            return render(request,'compras/pedidos/realizar_pedido.html',{'productos':produc,'idPedido':idPedido,'idProveedor':idProveedor,'detalle':detalle,'var':var})
    else:
        form=formulario()
        contexto={'form':form,'producto':producto,'idPedido':idPedido,'idProveedor':idProveedor,'idLinea':idLinea}
        return render(request,'compras/pedidos/realizar_pedido.html',contexto)

@login_required
def agregarPedido(request):#genera el pedido
    if request.method=='POST':
        fomu=pedidoForm(request.POST)
        if fomu.is_valid():
            form_data=fomu.cleaned_data
            pedido=Pedido()
            pedido.save()
            pago=Pago()
            pago.setfk_Pedido(pedido)
            pago.setFecha(date.today())
            var=str(form_data.get("tipo").get())
            pago.set_fk_Tipo(Tipo_Pago.objects.get(tipo=var))
            pago.save()
            pedido.fkProveedor=Proveedor.objects.get(nombre=form_data.get("proveedores").get())
            pedido.save()
            urlss='/compras/pedir/'+str(pedido.id)+'/'+str(Proveedor.objects.get(nombre=form_data.get("proveedores").get()).id)
            return redirect(urlss)
    else:
        form=pedidoForm()
        return render(request,'compras/pedidos/generar_pedidos.html',{'form':form})

@login_required
def agregarLinea(request,  idPedido, producto, idProveedor):#agrega las líneas de pedido
    if request.method=='POST':
        fom=formulario(request.POST)
        if fom.is_valid():
            form_data=fom.cleaned_data
            detalle=detalle_Pedido()
            pedido=Pedido.objects.get(id=idPedido)
            producto=Producto.objects.get(id=producto)
            detalle.setfkPedido(pedido)
            detalle.setfkProducto(producto)
            detalle.setCantidad(form_data.get("cantidad"))
            detalle.setSubtotal()
            pedido.agregarSubtotal(detalle.getSubtotal())
            detalle.setComentario(form_data.get("comentario"))
            detalle.save()
            pedido.save()
            cat=Categoria.objects.get(id=idProveedor)
            produc=Producto.objects.all().filter(fkcategoria= cat)
            detalle=detalle_Pedido.objects.all().filter(fkPedido=Pedido.objects.get(id=idPedido))
            var=detalle.count()
            return render(request,'compras/pedidos/realizar_pedido.html',{'productos':produc,'idPedido':idPedido,'idProveedor':idProveedor,'detalle':detalle,'var':var})
    else:
        form=formulario()
        contexto={'form':form,'idPedido':idPedido, 'producto':producto,'idProveedor':idProveedor}
        return render(request,'compras/pedidos/agregar_articulo.html',contexto)

@login_required
class PedidosList(ListView):
    model = detalle_Pedido
    template_name = 'compras/pedidos/gestionar_pedidos.html'

@login_required
class PedidosCreate(CreateView):
    model = detalle_Pedido
    form_class = pedidoForm
    template_name = 'compras/pedidos/generar_pedidos.html'
    success_url = reverse_lazy('compras:reCom')