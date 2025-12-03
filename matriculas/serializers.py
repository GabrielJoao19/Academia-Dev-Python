from rest_framework import serializers
from .models import Matricula

class MatriculaSerializer(serializers.ModelSerializer):
    status_descricao = serializers.ReadOnlyField()

    class Meta:
        model = Matricula
        fields = (
            'id',
            'aluno',
            'curso',
            'status',
            'status_descricao',
        )