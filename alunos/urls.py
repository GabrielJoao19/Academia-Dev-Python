from django.urls import path
from .views import AlunosVIEW, AlunoEdicaoView, AlunoExclusaoView

app_name = 'alunos'

urlpatterns = [
   path('', AlunosVIEW.as_view(), name='alunos'),
   path('editar/<int:aluno_id>/', AlunoEdicaoView.as_view(), name='editar_aluno'),
   path('excluir/<int:aluno_id>/', AlunoExclusaoView.as_view(), name='excluir_aluno'),
]