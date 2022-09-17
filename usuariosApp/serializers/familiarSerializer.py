from usuariosApp.models.familiar import Familiar
from rest_framework import serializers

class FamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Familiar
        fields = ['nombre', 'apellido', 'telefono', 'genero', 'parentesco', 'email']