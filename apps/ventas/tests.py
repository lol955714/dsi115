from django.test import TestCase, Client
from django.urls import reverse, resolve, path
import json
from .models import Empleado
from .views import empleado_list, save_empleado_form, empleado_create, empleado_update, empleado_delete
from .forms import EmpleadoForm



class EmpleadoTest(TestCase):
    def setUp(self):
        self.cliente = Client()
        Empleado.objects.create(
            clave='1234',
            nombres='Juan Antonio', 
            apellidos='Perez',
            telefono='87545129',
            dui='084578569',
            nit='12457889561245',
        )

    def test_create_empleado(self):
        empleado1 = Empleado.objects.get(clave="1234")
        self.assertEqual(empleado1.nombres, 'Juan Antonio')

    def test_form_valid_data(self):
        form = EmpleadoForm(data={
            'clave':'5555',
			'nombres':'Luisa',
			'apellidos':'Trujillo',
			'telefono':'77775558',
			'dui':'084578561',
			'nit':'44457889561245',
        })
        self.assertTrue(form.is_valid())

    def url_test_empleado_list(self):
        url = reverse('ventas:empleado-list')
        print(resolve(url))
        self.assertEqual(resolve(url),empleado_list)

    def url_test_empleado_update(self):
        empleado1 = Empleado.objects.get(clave="1234")
        url = reverse('ventas:empleado-update',args=[empleado1.id])
        self.assertEqual(resolve(url).func,empleado_update)



        
        