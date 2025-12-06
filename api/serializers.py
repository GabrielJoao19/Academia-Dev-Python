from rest_framework import serializers
from alunos.models import Aluno
from cursos.models import Curso
from matriculas.models import Matricula

#MATRICULA SERIALIZER
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

#CURSO SERIALIZER
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

#ALUNO SERIALIZER
class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = (
            'id',
            'nome',
            'email',
            'cpf',
        )