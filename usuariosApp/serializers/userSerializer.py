from rest_framework import serializers
from usuariosApp.models.user import User
from usuariosApp.models.familiar import Familiar
from usuariosApp.models.medico import Medico
from usuariosApp.serializers.familiarSerializer import FamiliarSerializer
from usuariosApp.serializers.medicoSerializer import MedicoSerializer

class UserSerializer(serializers.ModelSerializer):
    familiar = FamiliarSerializer()
    medico = MedicoSerializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'name', 'email']

    def create(self, validated_data):
        userInstance = User.objects.create(**validated_data)
        Medico.objects.create(user=userInstance)
        return userInstance

    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        familiar = Familiar.objects.get(user=obj.id)
        medico = Medico.objects.get(user=obj.id)
        return {
            'id': user.id,
            'username': user.username,
            'name': user.name,
            'email': user.email
        }