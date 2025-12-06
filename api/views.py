from rest_framework import generics
from alunos.models import Aluno
from cursos.models import Curso
from matriculas.models import Matricula
from .serializers import MatriculaSerializer, CursoSerializer, AlunoSerializer
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from .services import AcademiaService
from django.http import JsonResponse

#MATRICULA VIEWS
class MatriculasAPIView(generics.ListCreateAPIView):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

    def get_queryset(self):
        if self.kwargs.get('aluno_pk'):
            return self.queryset.filter(aluno_id=self.kwargs['aluno_pk'])
        return self.queryset.all()

class MatriculaAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

    def get_object(self):
        if self.kwargs.get('aluno_pk'):
           return get_object_or_404(self.get_queryset(), aluno_id=self.kwargs['aluno_pk'], pk=self.kwargs.get('matricula_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('matricula_pk'))
    
#Aluno VIEWS
class AlunosAPIView(generics.ListCreateAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class AlunoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

#CURSO VIEWS
class CursosAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

srv = AcademiaService() 

class AcademiaViewSet(viewsets.ViewSet):

    def matriculas_por_curso(self, request):
        dados = srv.total_matriculas_por_curso()
        return Response(dados)

    def total_devido_por_aluno(self, request):
        dados = srv.total_devido_por_aluno()
        return Response(dados)

    def pagamentos_pendentes(self, request):
        total = srv.total_pagamentos_pendentes()
        dados = {
            'nome_relatorio': 'Valor Total Devido (Pagamentos Pendentes)',
            'valor_total': total
        }
        return Response(dados)
    
    def sql_bruto_devido(self, request):
        sql_query = """
        SELECT
            T1.id, 
            T1.nome AS aluno_nome,
            SUM(T3.valor_inscricao) AS total_devido
        FROM
            alunos_aluno AS T1          
        JOIN
            matriculas_matricula AS T2  
            ON T1.id = T2.aluno_id
        JOIN
            cursos_curso AS T3          
            ON T2.curso_id = T3.id
        WHERE
            T2.status = 0
        GROUP BY
            T1.id, T1.nome
        HAVING
            total_devido > 0;
        """
        resultados = Aluno.objects.raw(sql_query)
        
        dados_json = []
        for resultado in resultados:
            dados_json.append({
                'aluno_id': resultado.id,
                'aluno_nome': resultado.aluno_nome,
                'total_devido': float(resultado.total_devido) 
            })
            
        return Response(dados_json)