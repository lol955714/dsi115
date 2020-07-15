from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

#librerias usadas para articulo y proveedor
from .forms	import ProveedorForm, ArticuloForm		
from apps.inventario.models import Proveedor, Producto
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string

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
