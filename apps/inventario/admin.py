from django.contrib import admin

# Register your models here.
from .models import *
'''
admin.site.register(Categoria)

admin.site.register(Proveedor)

admin.site.register(Producto)

admin.site.register(CategoriaIncidencia)

admin.site.register(Incidencia)
'''

admin.sites.AdminSite.site_header = 'Administración del sistema SIAVAC'
admin.sites.AdminSite.site_title = 'SIAVAC Administracion'
admin.sites.AdminSite.index_title = ''
