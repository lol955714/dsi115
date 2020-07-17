from __future__ import unicode_literals
from __future__ import absolute_import
from django.conf.urls import url
from apps.inventario.views import *
app_name='inventario'
urlpatterns=[
url(r'^inventario',inventario,name="inventario"),
url(r'^editar_producto/(?P<idProducto>\w+)', gestprod2, name="gestprod"),
url(r'^eliminar_producto/(?P<idProducto>\w+)',deleteprod, name="elimprod"),
]