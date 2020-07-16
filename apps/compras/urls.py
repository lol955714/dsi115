from __future__ import unicode_literals
from __future__ import absolute_import
from django.urls import path
from django.conf.urls import url
from apps.compras.views import *

app_name='compras'
urlpatterns=[
    url(r'^index',verpedidos,name="index"),
    url(r'^realizarCompras',agregarPedido,name="reCom"),
    #url(r'^addPedido', agregarPedido, name="addP"),
    url(r'^gestionarPedidos',PedidosList.as_view(),name="gesPed"),
    path(
    	'proveedor/', 
    	proveedor_list,
    	name='proveedor-list'
    ),
    path(
    	'proveedor/create/',
    	proveedor_create,
    	name='proveedor-create'
    ),
    path(
        'proveedor/update/<int:pk>',
        proveedor_update,
        name='proveedor-update'
    ),
    path(
        'proveedor/delete/<int:pk>',
        proveedor_delete,
        name='proveedor-delete'
    ),


    path(
    	'articulo/', 
    	articulo_list,
    	name='articulo-list'
    ),
    path(
    	'articulo/create/',
    	articulo_create,
    	name='articulo-create'
    ),
    path(
        'articulo/update/<int:pk>',
        articulo_update,
        name='articulo-update'
    ),
    path(
        'articulo/delete/<int:pk>',
        articulo_delete,
        name='articulo-delete'
    ),

]