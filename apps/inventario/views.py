from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.views.generic import *
from django.shortcuts import *
from apps.inventario.forms import *

# Create your views here.

@login_required
def inventario(request):
	producto=Producto.objects.all()
	contexto={'productos':producto}
	return render(request,'base/existencias.html',contexto)

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

def deleteprod(request,idProducto):
    producto = Producto.objects.get(id=idProducto)
    if request.method=='POST':
        form = elimiarForm(request.POST)
        if form.is_valid():
             producto.delete()
             return redirect('inventario:inventario')
    form = elimiarForm()
    return render(request, 'inventario/eliminar_producto.html',{'form':form,'idProducto':idProducto})