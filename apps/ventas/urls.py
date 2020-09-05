from __future__ import unicode_literals
from __future__ import absolute_import
from django.urls import path
from django.conf.urls import url
from apps.seguridad.views import *
from django.contrib.auth.views import LogoutView
app_name='ventas'
urlpatterns=[
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


]