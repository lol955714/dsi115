from __future__ import unicode_literals
from __future__ import absolute_import
from django.urls import path
from django.conf.urls import url
from apps.seguridad.views import *
from apps.ventas.views import *
from django.contrib.auth.views import LogoutView
app_name='ventas'
urlpatterns=[
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
        'empleado/meta/',
        informe_meta,
        name='empleado-meta'
    )
]