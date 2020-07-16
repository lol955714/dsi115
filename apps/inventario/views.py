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

def gestprod(request,idProducto):
    producto = Producto.objects.get(id=idProducto)
    if request.method == 'GET':
        form = productoForm(instance=producto)
    else:
        form = productoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
        return redirect('inventario:inventario')
    return render(request, 'inventario/modificar_producto.html',{'form':form,'idProducto':idProducto})
