from django.test import TestCase, Client
from django.urls import reverse
from apps.inventario.models import *



class TestViews(TestCase):

	def test_inventario_GET(self):
		producto=Producto.objects.create()

		response =producto.get(reverse('inventario'))


		self.assertEquals(response.status_code,200)
		self.asserTemplateUsed(response,'base/existencias.html')

