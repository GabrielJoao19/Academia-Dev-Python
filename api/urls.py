from django.urls import path
from .views import MatriculaAPIView, MatriculasAPIView, CursosAPIView, CursoAPIView, AlunosAPIView, AlunoAPIView, AcademiaViewSet
from . import views

app_name = 'api'

urlpatterns = [
    path('matriculas/', MatriculasAPIView.as_view(), name='matriculas'),
    path('matriculas/<int:pk>/', MatriculaAPIView.as_view(), name='matricula'), ## Editar, deletar uma matricula especifica
    path('alunos/<int:aluno_pk>/matriculas', MatriculasAPIView.as_view(), name='matriculas_por_aluno'),
    path('alunos/<int:aluno_pk>/matriculas/<int:matricula_pk>/', MatriculaAPIView.as_view(), name='matricula_por_aluno'),
    path('alunos/', AlunosAPIView.as_view(), name='alunos'),
    path('alunos/<int:pk>/', AlunoAPIView.as_view(), name='aluno'),
    path('cursos/', CursosAPIView.as_view(), name='cursos'),
    path('cursos/<int:pk>/', CursoAPIView.as_view(), name='curso'),
    path('relatorios/matriculas-curso/', AcademiaViewSet.as_view({'get': 'matriculas_por_curso'}), name='api_matriculas_curso'),
    path('relatorios/devido-aluno/', AcademiaViewSet.as_view({'get': 'total_devido_por_aluno'}), name='api_devido_aluno'),
    path('relatorios/pendentes/', AcademiaViewSet.as_view({'get': 'pagamentos_pendentes'}), name='api_pagamentos_pendentes'),
    path('relatorios/sql-bruto-devido/', AcademiaViewSet.as_view({'get': 'sql_bruto_devido'}), name='api_sql_bruto_devido'),


]

