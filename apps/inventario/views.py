from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.

@login_required
def inventario(request):
	producto=Producto.objects.all()
	contexto={'productos':producto}
	return render(request,'base/existencias.html',contexto)
