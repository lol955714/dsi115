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
from django.db.models import Q
from django.db.models import Count
from django.contrib.humanize.templatetags.humanize import intcomma

import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

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
    #metodo que recupera lo mandado en la barra de buscar
    buscar=request.POST.get("buscar")
    lineas = lineaDeVenta.objects.filter(pedidofk=int(idPedido))
    pedid = pedido.objects.get(id=int(idPedido))
    error=pedid.nope
    pedid.errorContra()
    pedid.save()
    if buscar:
        #funcion que busca por nombre 
        productos=Producto.objects.filter(Q(nombre__icontains=buscar))
    else: 
      productos = Producto.objects.all()
    return render(request,'ventas/venta/factura.html',{'pedid':pedid,'lineas':lineas, 'productos':productos,'error':error})

def finalizarVenta(request,idPedido):
    ped=pedido.objects.get(id=int(idPedido))
    if request.method=='POST':
        con=contra(request.POST)
        if con.is_valid():
            datos=con.cleaned_data
            try: 
                emple=Empleado.objects.get(clave=datos.get("passwd"))
                print("hola")
                ped.setFinal()
                ped.setVendedor(emple)
                ped.setTipoPago(datos.get("typ").get())
                ped.save()
                return redirect('/')
            except:
                if ped.nope == False:
                    ped.nope=True
                    print("holi")
                    ped.save()
                return redirect('/ventas/vender/'+str(ped.id))   
    else:
        return render(request,'ventas/venta/confirmar.html',{'ped':ped,'form':contra()})

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
            venta.save()
            ruta='/ventas/vender/'+str(venta.id)
            return redirect(ruta)
    else:
        form=iniciarVe()
        return render(request,'ventas/venta/iniciarVenta.html',{'form':form})



@login_required
def informe_meta_diaria(request):
    mes_actual = datetime.now().month
    anio_actual = datetime.now().year
    dia_actual = datetime.now().day

    #obtiene el total de las ventas realizadas por empledado en un tiempo especifico
    meta_diaria = Asignacion.objects.filter(tipo_meta=1)
    totales = pedido.objects.filter(
        fechaCreada__year=anio_actual).values(
            'vendedor','vendedor__nombres','vendedor__apellidos','vendedor__id').annotate(Sum('total'))  
    
    return render(request,'ventas/informes/empleado_meta_diaria.html',
    {'totales':totales,'meta_diaria':meta_diaria})

@login_required
def informe_meta_diaria_pdf(request):
    template_path = 'ventas/informes/ventas_meta_diaria_pdf.html'

    anio_actual = datetime.now().year
    meta_diaria = Asignacion.objects.filter(tipo_meta=1)
    totales = pedido.objects.filter(
        fechaCreada__year=anio_actual).values(
            'vendedor','vendedor__nombres','vendedor__apellidos','vendedor__id').annotate(Sum('total'))  

    context = {'totales':totales,'meta_diaria':meta_diaria}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

@login_required
def informe_meta_quincenal(request):
    mes_actual = datetime.now().month
    anio_actual = datetime.now().year
    dia_actual = datetime.now().day

    #obtiene el total de las ventas realizadas por empledado en un tiempo especifico
    meta_diaria = Asignacion.objects.filter(tipo_meta=2)
    totales = pedido.objects.filter(
        fechaCreada__year=anio_actual).values(
            'vendedor','vendedor__nombres','vendedor__apellidos','vendedor__id').annotate(Sum('total'))  
    
    return render(request,'ventas/informes/empleado_meta_quincenal.html',
    {'totales':totales,'meta_diaria':meta_diaria})

@login_required
def informe_meta_quincenal_pdf(request):
    template_path = 'ventas/informes/ventas_meta_quincenal_pdf.html'

    anio_actual = datetime.now().year
    meta_diaria = Asignacion.objects.filter(tipo_meta=2)
    totales = pedido.objects.filter(
        fechaCreada__year=anio_actual).values(
            'vendedor','vendedor__nombres','vendedor__apellidos','vendedor__id').annotate(Sum('total'))  

    context = {'totales':totales,'meta_diaria':meta_diaria}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

@login_required
def informe_meta_mensual(request):
    mes_actual = datetime.now().month
    anio_actual = datetime.now().year
    dia_actual = datetime.now().day

    #obtiene el total de las ventas realizadas por empledado en un tiempo especifico
    meta_diaria = Asignacion.objects.filter(tipo_meta=3)
    totales = pedido.objects.filter(
        fechaCreada__year=anio_actual).values(
            'vendedor','vendedor__nombres','vendedor__apellidos','vendedor__id').annotate(Sum('total'))  
    
    return render(request,'ventas/informes/empleado_meta_mensual.html',
    {'totales':totales,'meta_diaria':meta_diaria})

@login_required
def informe_meta_mensual_pdf(request):
    template_path = 'ventas/informes/ventas_meta_mensual_pdf.html'

    anio_actual = datetime.now().year
    meta_diaria = Asignacion.objects.filter(tipo_meta=3)
    totales = pedido.objects.filter(
        fechaCreada__year=anio_actual).values(
            'vendedor','vendedor__nombres','vendedor__apellidos','vendedor__id').annotate(Sum('total'))  

    context = {'totales':totales,'meta_diaria':meta_diaria}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

@login_required
def informe_ventas_totales(request):
    anio_actual = datetime.now().year
    productos_vendidos = lineaDeVenta.objects.filter().values(
            'articulofk__id','articulofk__nombre').annotate(cant=Sum('cantidad'),sub=Sum('subtotal')).order_by('-cant') 
    total_vendido = pedido.objects.all().aggregate(Sum('total'))['total__sum']
    total = f"${intcomma('{:0.2f}'.format(total_vendido))}"
    return render(request,'ventas/empleado/ventas_totales.html',
    {'productos_vendidos':productos_vendidos,'total_vendido':total})

def informe_ventas_totales_pdf(request):
    template_path = 'ventas/informes/ventas_totales_pdf.html'
    context = {'productos_vendidos':lineaDeVenta.objects.filter().values(
            'articulofk__id','articulofk__nombre').annotate(cant=Sum('cantidad'),sub=Sum('subtotal')).order_by('-cant'),'total_vendido':pedido.objects.all().aggregate(Sum('total'))['total__sum']}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

@login_required
def informe_productos_categoria(request):
    anio_actual = datetime.now().year
    productos_vendidos_categoria = lineaDeVenta.objects \
        .values('articulofk__fkcategoria__nombre','articulofk__nombre') \
        .annotate(cant=Count('cantidad')).order_by('-cant') 
    return render(request,'ventas/informes/ventas_categoria.html',
    {'productos_vendidos_categoria':productos_vendidos_categoria})

@login_required
def informe_productos_categoria_pdf(request):
    template_path = 'ventas/informes/ventas_categoria_pdf.html'
    productos_vendidos_categoria = lineaDeVenta.objects \
        .values('articulofk__fkcategoria__nombre','articulofk__nombre') \
        .annotate(cant=Count('cantidad')).order_by('-cant') 
    context = {'productos_vendidos_categoria':productos_vendidos_categoria}
            
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


@login_required
def informe_existencia_productos(request):
    anio_actual = datetime.now().year
    productos_existencia = Producto.objects \
        .values('nombre','fkproveedor__nombre','fkcategoria__nombre','existencia') \
        .order_by('existencia') 
    return render(request,'ventas/informes/inventario.html',
    {'productos_existencia':productos_existencia})

@login_required
def informe_existencia_productos_pdf(request):
    template_path = 'ventas/informes/inventario_pdf.html'
    productos_existencia = Producto.objects \
        .values('nombre','fkproveedor__nombre','fkcategoria__nombre','existencia') \
        .order_by('existencia')  
    context = {'productos_existencia':productos_existencia}
            
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

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

