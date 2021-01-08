from __future__ import unicode_literals
from __future__ import absolute_import
from django.urls import path
from django.conf.urls import url
from apps.compras.views import *

app_name='compras'
urlpatterns=[
    url(r'^cancel/(?P<idPedido>\w+)',cancelarPedido,name="cancel"),
    url(r'^aceptar/(?P<idPedido>\w+)',recibirPedido,name="aceptar"),
    url(r'^index',verpedidos,name="index"),
    url(r'^realizarCompras',agregarPedido,name="reCom"),
    url(r'^add/(?P<idPedido>\w+)/(?P<producto>\w+)/(?P<idProveedor>\w+)', agregarLinea,name="add"),
    url(r'^editar/(?P<idLinea>\w+)/(?P<idPedido>\w+)/(?P<producto>\w+)/(?P<idProveedor>\w+)', editarLinea,name="editarLinea"),
    url(r'^borrar/(?P<idLinea>\w+)/(?P<idPedido>\w+)/(?P<producto>\w+)/(?P<idProveedor>\w+)', borrarLinea,name="borrarLinea"),
    #url(r'^addPedido', agregarPedido, name="addP"),
    url(r'^pedir/(?P<idPedido>\w+)/(?P<idProveedor>\w+)/', lineapedido, name="lin"),
    url(r'^cancelar/(?P<idPedido>\w+)/', cancelar, name="cancelar"),
    url(r'^verDetalle/(?P<idPedido>\w+)/', verDetalle, name="verDetalle"),
    url(r'^gestionarPedidos',PedidosList,name="gesPed"),
    
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