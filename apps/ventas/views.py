from .forms	import *
from .models import *
from apps.inventario.models import Producto, Proveedor, Categoria
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.db.models import Sum
from datetime import datetime

def eliminarPendientes(request):
    pedid=pedido.objects.filter(finalizada=False)
    if pedid.count()>0:
        pedid.delete()
    return redirect("/")

def sinFinalizar(request):
    pedidos=pedido.objects.filter(finalizada=False)
    return render(request,'ventas/venta/sinFinalizar.html',{'pedidos':pedidos})

def cancelarVenta(request,idPedido):
    pedid=pedido.objects.get(id=int(idPedido))
    print(pedid.total)
    if lineaDeVenta.objects.filter(pedidofk=pedid.id).count()>0:
        lineaDeVenta.objects.filter(pedidofk=pedid.id).delete()
    pedid.delete()
    return redirect("/")

def venta(request, idPedido):
    lineas = lineaDeVenta.objects.filter(pedidofk=int(idPedido))
    productos = Producto.objects.all()
    pedid = pedido.objects.get(id=int(idPedido))
    error=pedid.errorContra
    pedid.errorContra()
    pedid.save()
    return render(request,'ventas/venta/factura.html',{'pedid':pedid,'lineas':lineas, 'productos':productos,'error':error})

def finalizarVenta(request,idPedido):
    ped=pedido.objects.get(id=int(idPedido))
    if request.method=='POST':
        con=contra(request.POST)
        if con.is_valid():
            datos=con.cleaned_data
            credencial=pedido.objects.get(id=int(idPedido)).vendedor.usuario
            user=authenticate(username=credencial.username, password=datos.get("passwd"))
            if user != None:
                print("holi")
                ped.setFinal()
                ped.save()
                return redirect('/')
            else:
                ped.errorContra()
                ped.save()
                return redirect('/ventas/vender/'+str(ped.id))
    else:
        form=contra()
        return render(request,'ventas/venta/confirmar.html',{'form':form,'ped':ped})

def eliminarLinea(request, idLinea):
    var=lineaDeVenta.objects.get(id=int(idLinea))
    pedid=var.pedidofk
    pedid.quitar(var.getSubtotal())
    pedid.save()
    var.delete()
    return redirect('/ventas/vender/'+str(pedid.id))
     
def editarLinea(request, idLinea):
    linea=lineaDeVenta.objects.get(id=int(idLinea))
    if request.method == 'POST':
        form = agregar(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            pedid=linea.pedidofk
            pedid.quitar(linea.getSubtotal())
            linea.setCantidad(form_data.get("cantidad"))
            linea.sub()
            linea.save()
            pedid.setTotal(linea.getSubtotal())
            pedid.save()
            return redirect('/ventas/vender/'+str(linea.pedidofk.id))
    else:
        form=agregar()
        content={'form':form,'linea':linea}
    return render(request,'ventas/venta/editar.html',content)

def agregarLinea(request,idPedido,idProducto):
    pedid=pedido.objects.get(id=int(idPedido))
    prod=Producto.objects.get(id=int(idProducto))
    if request.method == 'POST':
        form=agregar(request.POST)
        if form.is_valid():
            form_data=form.cleaned_data
            linea=lineaDeVenta()
            linea.setArticulo(prod)
            linea.setCantidad(int(form_data.get("cantidad")))
            linea.setPedido(pedid)
            linea.sub()
            linea.save()
            pedid.setTotal(linea.getSubtotal())
            pedid.save()
            ruta='/ventas/vender/'+str(pedid.id)
            return redirect(ruta)
    else:
        form=agregar()
        variables={'form':form,'pedid':pedid,'prod':prod}
        return render (request,'ventas/venta/agregar.html',variables)

def iniciarVenta(request):
    if request.method =='POST':
        form=iniciarVe(request.POST)
        if form.is_valid():            
            form_data=form.cleaned_data
            venta=pedido()
            venta.setCliente(form_data.get("cliente"))
            venta.setVendedor(form_data.get("vendedor").get())
            venta.save()
            ruta='/ventas/vender/'+str(venta.id)
            return redirect(ruta)
    else:
        form=iniciarVe()
        return render(request,'ventas/venta/iniciarVenta.html',{'form':form})

@login_required
def informe_meta(request):
    mes_actual = datetime.now().month
    anio_actual = datetime.now().year
    dia_actual = datetime.now().day

    #obtiene el total de las ventas realizadas por empledado en un tiempo especifico
    totales = pedido.objects.filter(
        fechaCreada__year=anio_actual,fechaCreada__month=mes_actual).values(
            'vendedor__nombres').annotate(Sum('total'))  
    
    pedidos = Metas.objects.filter(descripcion='hola').aggregate(Sum('monto_asignado'))
    return render(request,'ventas/empleado/empleado_metas.html',
    {'pedidos':pedidos, 'totales':totales})

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
        data['html_meta_list'] = render_to_string('ventas/meta/meta_list_2.html', {
            'metas': metas
        })
    else:
        context = {'meta': meta}
        data['html_form'] = render_to_string('ventas/meta/meta_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)

@login_required
def asignacion_list(request):
	asignaciones = Asignacion.objects.all()
	return render(request,'ventas/asignacion/asignacion_list.html',{'asignaciones':asignaciones})

@login_required 
def save_asignacion_form(request, form, template_name):
	data = dict()
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			data['form_is_valid']=True
			asignaciones = Asignacion.objects.all()
			data['html_asignacion_list'] = render_to_string('ventas/asignacion/asignacion_list_2.html',
				{'asignaciones':asignaciones})
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
def asignacion_create(request):
    if request.method == 'POST':
        form = AsignacionForm(request.POST)
    else:
        form = AsignacionForm()
    return save_asignacion_form(request, form, 'ventas/asignacion/asignacion_create.html')

@login_required
def asignacion_update(request, pk):
    asignacion = get_object_or_404(Asignacion, pk=pk)
    if request.method == 'POST':
        form = AsignacionForm(request.POST, instance=asignacion)
    else:
        form = AsignacionForm(instance=asignacion)
    return save_asignacion_form(request, form, 'ventas/asignacion/asignacion_update.html')
    
@login_required
def asignacion_delete(request, pk):
    asignacion = get_object_or_404(Asignacion, pk=pk)
    data = dict()
    if request.method == 'POST':
        asignacion.delete()
        data['form_is_valid'] = True  
        asignaciones = Asignacion.objects.all()
        data['html_asignacion_list'] = render_to_string('ventas/asignacion/asignacion_list_2.html', {
            'asignaciones': asignaciones
        })
    else:
        context = {'asignacion': asignacion}
        data['html_form'] = render_to_string('ventas/asignacion/asignacion_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)

