from rest_framework import serializers
from .models import Curso

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = (
            'id',
            'nome',
            'carga_horaria',
            'valor_inscricao',
            'status',
        )