from django.db import models

# Create your models here.
from django.db import models
class FeriadoModel(models.Model):
 name = models.CharField('Feriado',max_length=50)
 date = models.IntegerField('Data')
 ano = models.IntegerField('Mês')

 modificado_em = models.DateTimeField(
 verbose_name='modificado em',
 auto_now_add=False, auto_now=True)

 def __str__(self):
    return self.name