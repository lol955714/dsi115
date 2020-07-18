from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from .models import *
from django.views.generic import *
from django.shortcuts import *
from apps.inventario.forms import *

# Create your views here.

@login_required
def inventario(request):
	global contexto
	buscar=request.POST.get("buscar")
	control=Producto.objects.filter(Q(existencia__lte=5))
	if buscar:
	 	producto=Producto.objects.filter(Q(nombre__icontains=buscar))
	 	contexto={'productos':producto}
	elif control:
	    contexto={'productos':control}
	    messages.info(request,"Los siguientes productos tienen existencias bajas")
	else:
		producto=Producto.objects.all()
		contexto={'productos':producto}

	return render(request,'base/existencias.html',contexto)

@login_required
def gestprod2(request,idProducto):
    producto = Producto.objects.get(id=idProducto)
    if request.method=='POST':
        form = productoForm(request.POST, instance=producto)
        if form.is_valid():
             form.save()
             form_data=form.cleaned_data
             incid = Incidencia()
             incid.setDescripcion(form_data.get("comentario"))
             incid.setCategoriaIncidencia(form_data.get("fkcate"))
             incid.setProducto(producto)
             incid.save()
             return redirect('inventario:inventario')
    form = productoForm(instance=producto)
    producto = Producto.objects.get(id=idProducto)
    return render(request, 'inventario/modificar_producto.html',{'form':form,'idProducto':idProducto})

@login_required
def deleteprod(request,idProducto):
    producto = Producto.objects.get(id=idProducto)
    if request.method=='POST':
        form = elimiarForm(request.POST)
        if form.is_valid():
             producto.delete()
             return redirect('inventario:inventario')
    form = elimiarForm()
    return render(request, 'inventario/eliminar_producto.html',{'form':form,'idProducto':idProducto})