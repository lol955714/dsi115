from __future__ import unicode_literals
from __future__ import absolute_import
from django.conf.urls import url
from apps.compras.views import *
app_name='compras'
urlpatterns=[
url(r'^index',indexCompras,name="index")
]