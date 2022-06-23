from django.test import TestCase
from feriado.models import FeriadoModel

# Create your tests here.
class FeriadoTest(TestCase):
 def setUp(self):
  self.resp = self.client.get('/')

 def test_200_response(self):
  self.assertEqual(200, self.resp.status_code)
  
 def test_texto(self):
  self.assertContains(self.resp, 'feriado')


class FeriadoModelTest(TestCase):
 def setUp(self):
  self.feriado = 'Natal'
  self.mes = 12
  self.dia = 25
  self.cadastro = FeriadoModel(
  nome=self.feriado,
  dia=self.dia,
  mes=self.mes,
 )
  self.cadastro.save()
