from rest_framework import serializers
from cpyg.models import Cliente
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model= Cliente
        fields=['rut', 'nombre', 'correo', 'telefono', 'direccion']