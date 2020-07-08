from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
#falta agregar verificación por rol
@login_required
def indexCompras(request):
	return render(request,'compras/index.html')