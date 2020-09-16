from .forms	import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.db.models import Sum


def iniciarVenta(request):
    if request.method =='POST':
        formulario=iniciarVe(request.POST)
        if form.is_valid():            
            form_data=formulario.cleaned_data
            venta=pedido()
            venta.setCliente(form_data.get("cliente"))
            venta.setVendedor(Empleado.objects.get(id=form_data.get("vendedor").get()))
            venta.save()
            return render(request,'ventas/venta/edicionPedido.html',{'valor':venta.id})
    else:
        formulario=iniciarVe()
        return render(request,'ventas/venta/iniciarVenta.html',{'form':iniciarVe})




@login_required
def empleado_list(request):
	empleados = Empleado.objects.all()
	return render(request,'ventas/empleado/empleado_list.html',{'empleados':empleados})

@login_required
def save_empleado_form(request, form, template_name):
	data = dict()
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			data['form_is_valid']=True
			empleados = Empleado.objects.all()
			data['html_empleado_list'] = render_to_string('ventas/empleado/empleado_list_2.html',
				{'empleados':empleados})
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
def empleado_create(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
    else:
        form = EmpleadoForm()
    return save_empleado_form(request, form, 'ventas/empleado/empleado_create.html')

@login_required
def empleado_update(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
    else:
        form = EmpleadoForm(instance=empleado)
    return save_empleado_form(request, form, 'ventas/empleado/empleado_update.html')
    
@login_required
def empleado_delete(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    data = dict()
    if request.method == 'POST':
        empleado.delete()
        data['form_is_valid'] = True  
        empleados = Empleado.objects.all()
        data['html_empleado_list'] = render_to_string('ventas/empleado/empleado_list_2.html', {
            'empleados': empleados
        })
    else:
        context = {'empleado': empleado}
        data['html_form'] = render_to_string('ventas/empleado/empleado_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)

@login_required
def meta_list(request):
	metas = Metas.objects.all()
	return render(request,'ventas/meta/meta_list.html',{'metas':metas})

@login_required 
def save_meta_form(request, form, template_name):
	data = dict()
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			data['form_is_valid']=True
			metas = Metas.objects.all()
			data['html_meta_list'] = render_to_string('ventas/meta/meta_list_2.html',
				{'metas':metas})
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
def meta_create(request):
    if request.method == 'POST':
        form = MetaForm(request.POST)
    else:
        form = MetaForm()
    return save_meta_form(request, form, 'ventas/meta/meta_create.html')

@login_required
def meta_update(request, pk):
    meta = get_object_or_404(Metas, pk=pk)
    if request.method == 'POST':
        form = MetaForm(request.POST, instance=meta)
    else:
        form = MetaForm(instance=meta)
    return save_meta_form(request, form, 'ventas/meta/meta_update.html')
    
@login_required
def meta_delete(request, pk):
    meta = get_object_or_404(Metas, pk=pk)
    data = dict()
    if request.method == 'POST':
        meta.delete()
        data['form_is_valid'] = True  
        metas = Metas.objects.all()
        data['html_empleado_list'] = render_to_string('ventas/meta/meta_list_2.html', {
            'metas': metas
        })
    else:
        context = {'meta': meta}
        data['html_form'] = render_to_string('ventas/meta/meta_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)

