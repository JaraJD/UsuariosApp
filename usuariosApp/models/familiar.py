from django.db import models

class Familiar(models.Model):
    id = models.AutoField(primary_key=True, blank=False)
    nombre = models.CharField('Nombre',max_length=40)
    apellido = models.CharField('Apellido',max_length=40, null=True)
    telefono = models.IntegerField(default=0)
    genero = models.CharField(max_length=1)
    parentesco = models.CharField('Parentesco',max_length=100)
    email = models.EmailField('Email', max_length = 100)