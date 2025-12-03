from django.urls import path
from .views import MatriculaAPIView, MatriculasAPIView

app_name = 'matriculas'

urlpatterns = [
    path('matriculas/', MatriculasAPIView.as_view(), name='matriculas'),
    path('matriculas/<int:pk>/', MatriculaAPIView.as_view(), name='matricula'), ## Editar, deletar uma matricula especifica
    path('alunos/<int:aluno_pk>/matriculas', MatriculasAPIView.as_view(), name='matriculas_por_aluno'),
    path('alunos/<int:aluno_pk>/matriculas/<int:matricula_pk>/', MatriculaAPIView.as_view(), name='matricula_por_aluno'),
]

