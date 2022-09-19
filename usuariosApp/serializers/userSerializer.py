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
        fields = ['id', 'username', 'password', 'name', 'email', 'familiar', 'medico']

    def create(self, validated_data):
        familiarData = validated_data.pop('familiar')
        userInstance = User.objects.create(**validated_data)
        Familiar.objects.create(user=userInstance, **familiarData)
        return userInstance

    def create(self, validated_data):
        medicoData = validated_data.pop('medico')
        userInstance = User.objects.create(**validated_data)
        Medico.objects.create(user=userInstance, **medicoData)
        return userInstance

    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        familiar = Familiar.objects.get(user=obj.id)
        medico = Medico.objects.get(user=obj.id)
        return {
            'id': user.id,
            'username': user.username,
            'name': user.name,
            'email': user.email,
            'familiar': {
                'id': familiar.id,
                'nombre': familiar.nombre,
                'apellido': familiar.apellido,
                'telefono': familiar.telefono,
                'genero': familiar.genero,
                'parentesco': familiar.parentesco,
                'email': familiar.email
            },
            'medico': {
                'id': medico.id,
                'nombre': medico.nombre,
                'apellido': medico.apellido,
                'telefono': medico.telefono,
                'genero': medico.genero,
                'especialidad': medico.especialidad,
                'registro': medico.registro
            }
        }