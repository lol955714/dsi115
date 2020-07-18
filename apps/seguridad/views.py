from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



# Create your views here.

def auth(request):
	if request.method == 'POST':
		usern=request.POST.get('user',None)
		passw=request.POST.get('pass',None)
		user = authenticate(username=usern,password=passw)
		print(request.user.is_staff)
		if user is not None:
			login(request, user)#inicio de selección de index
			if request.user.groups.filter(name='administrador').exists():
				print("hola")
				return redirect('inventario:inventario')
			else:
				if request.user.is_staff == True:
					return redirect ("/admin")
				else:
					return render(request,'base/nope.html',{})#finaliza selección de index
		
	return render(request,'seguridad/login.html',{})



