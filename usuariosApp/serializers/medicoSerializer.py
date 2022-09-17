from usuariosApp.models.medico import Medico
from rest_framework import serializers

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ['nombre', 'apellido', 'telefono', 'genero', 'especialidad', 'registro']