from rest_framework import serializers
from core.models import Colaborador

class ColaboradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colaborador
        fields = ['rut', 'nombres', 'cargo']
