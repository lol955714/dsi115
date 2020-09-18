from __future__ import unicode_literals
from __future__ import absolute_import
from django.conf.urls import url
from apps.seguridad.views import *
from django.contrib.auth.views import LogoutView
app_name='seguridad'
urlpatterns=[
url(r'^index', index, name="index"),
url(r'^login', auth, name="ingresar"),
url(r'^logout', LogoutView.as_view(next_page='seguridad:ingresar'), name="logout"),
]