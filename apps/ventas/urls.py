from __future__ import unicode_literals
from __future__ import absolute_import
from django.urls import path
from django.conf.urls import url
from apps.seguridad.views import *
from apps.ventas.views import *
from django.contrib.auth.views import LogoutView
app_name='ventas'
urlpatterns=[
    url(r'^eliminarPendientes/', eliminarPendientes,name="eliminarPendientes"),
    url(r'^sinFinalizar/', sinFinalizar,name="sinFinalizar"),
    url(r'^iniciarVenta/', iniciarVenta,name="iniciar"),
    url(r'^vender/(?P<idPedido>\w+)', venta,name="vender"),
    url(r'^final/(?P<idPedido>\w+)', finalizarVenta,name="finalizar"),
    url(r'^cancelar/(?P<idPedido>\w+)', cancelarVenta,name="cancelar"),
    url(r'^añadir/(?P<idPedido>\w+)/(?P<idProducto>\w+)', agregarLinea,name="añadir"),
    url(r'^editar/(?P<idLinea>\w+)/', editarLinea,name="editar"),
    url(r'^eliminar/(?P<idLinea>\w+)/', eliminarLinea,name="eliminar"),
    path(
    	'empleado/', 
    	empleado_list,
    	name='empleado-list'
    ),
    path(
    	'empleado/create/',
    	empleado_create,
    	name='empleado-create'
    ),
    path(
        'empleado/update/<int:pk>',
        empleado_update,
        name='empleado-update'
    ),
    path(
        'empleado/delete/<int:pk>',
        empleado_delete,
        name='empleado-delete'
    ),

    path(
    	'meta/', 
    	meta_list,
    	name='meta-list'
    ),
    path(
    	'meta/create/',
    	meta_create,
    	name='meta-create'
    ),
    path(
        'meta/update/<int:pk>',
        meta_update,
        name='meta-update'
    ),
    path(
        'meta/delete/<int:pk>',
        meta_delete,
        name='meta-delete'
    ),
    path(
    	'asignacion/', 
    	asignacion_list,
    	name='asignacion-list'
    ),
    path(
    	'asignacion/create/',
    	asignacion_create,
    	name='asignacion-create'
    ),
    path(
        'asignacion/update/<int:pk>',
        asignacion_update,
        name='asignacion-update'
    ),
    path(
        'asignacion/delete/<int:pk>',
        asignacion_delete,
        name='asignacion-delete'
    ),

    path(
        'productos/categoria/',
        informe_productos_categoria,
        name='productos-categoria'
    ),

    #INFORMES 

    #ventas por producto
    path(
        'ventas/totales/',
        informe_ventas_totales,
        name='ventas-totales'
    ),
    path(
        'ventas/totales/pdf',
        informe_ventas_totales_pdf,
        name='ventas-totales-pdf'
    ),

    #ventas por categoria
    path(
        'informe/categoria/',
        informe_productos_categoria,
        name='informe-categoria'
    ),
    path(
        'informe/categoria/pdf',
        informe_productos_categoria_pdf,
        name='informe-categoria-pdf'
    ),

    #inventarios
    path(
        'informe/existencia/',
        informe_existencia_productos,
        name='informe-existencia'
    ),
    path(
        'informe/existencia/pdf',
        informe_existencia_productos_pdf,
        name='informe-existencia-pdf'
    ),

    #metas diarias
    path(
        'meta/diaria',
        informe_meta_diaria,
        name='empleado-meta-diaria'
    ),
    path(
        'meta/diaria/pdf',
        informe_meta_diaria_pdf,
        name='ventas-meta_diaria-pdf'
    ),
    path(
        'meta/quincenal',
        informe_meta_quincenal,
        name='empleado-meta-quincenal'
    ),
    path(
        'meta/quincenal/pdf',
        informe_meta_quincenal_pdf,
        name='ventas-meta_quincenal-pdf'
    ),
    path(
        'meta/mensual',
        informe_meta_mensual,
        name='empleado-meta-mensual'
    ),
    path(
        'meta/mensual/pdf',
        informe_meta_mensual_pdf,
        name='ventas-meta_mensual-pdf'
    ),
]