from __future__ import unicode_literals
from __future__ import absolute_import
from django.conf.urls import url
from apps.inventario.views import *
app_name='inventario'
urlpatterns=[
url(r'^inventario', inventario ,name="inventario"),
url(r'^inventario2', inventarioSinLog ,name="inventario2"),
url(r'^inventario',inventario,name="consulta"),	
url(r'^notificaciones',notificaciones,name="notif"),
url(r'^cuentas',cuentas,name="cuent"),
url(r'^editar_producto/(?P<idProducto>\w+)', gestprod2, name="gestprod"),
url(r'^eliminar_producto/(?P<idProducto>\w+)',deleteprod, name="elimprod"),
url(r'^editar_cuenta/(?P<idCuenta>\w+)', gestcuent, name="gestcuent"),
url(r'^eliminar_cuenta/(?P<idCuenta>\w+)',deletecuent, name="elimcuent"),
url(r'^addcuenta/', addcuenta, name="addcuent"),
]