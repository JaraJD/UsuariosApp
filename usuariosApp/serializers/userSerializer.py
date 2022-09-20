from rest_framework import serializers
from usuariosApp.models.user import User
from usuariosApp.models.familiar import Familiar
from usuariosApp.models.medico import Medico
from usuariosApp.models.account import Account
from usuariosApp.serializers.familiarSerializer import FamiliarSerializer
from usuariosApp.serializers.medicoSerializer import MedicoSerializer

class UserSerializer(serializers.ModelSerializer):
    familiar = FamiliarSerializer()
    medico = MedicoSerializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'name', 'email', 'account']

    def create(self, validated_data):
        accountData = validated_data.pop('account')
        userInstance = User.objects.create(**validated_data)
        Account.objects.create(user=userInstance, **accountData)
        return userInstance

    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        account = Account.objects.get(user=obj.id)
        return {
            'id': user.id,
            'username': user.username,
            'name': user.name,
            'email': user.email,
            'account': {
                'id': account.id,
                'cargo': account.cargo
            }
        }