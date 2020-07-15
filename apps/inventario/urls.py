from __future__ import unicode_literals
from __future__ import absolute_import
from django.conf.urls import url
from apps.inventario.views import *
app_name='inventario'
urlpatterns=[
url(r'^inventario',inventario,name="inventario")
]