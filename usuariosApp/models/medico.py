from django.db import models
from .user import User

class Medico(models.Model):
    id = models.AutoField(primary_key=True, blank=False)
    nombre = models.CharField('Nombre',max_length=40)
    apellido = models.CharField('Apellido',max_length=40)
    telefono = models.IntegerField (default=0)
    Genero=(("m","Masculino"),("f","Femenino"))
    genero = models.CharField(max_length=1,choices=Genero, help_text='Seleccione el genero )')
    especialidad = models.CharField(max_length=100)
    registro = models.CharField(max_length=100)
    user = models.ForeignKey(User, related_name='paciente_medico', on_delete=models.CASCADE)