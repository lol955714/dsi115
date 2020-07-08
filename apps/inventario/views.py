from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def indexInentario(request):
	return render(request,'inventario/index.html')
