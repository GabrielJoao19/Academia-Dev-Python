from django.urls import path
from .views import CursosVIEW, CursoEdicaoView, CursoExclusaoView
app_name = 'cursos'

urlpatterns = [
   path('', CursosVIEW.as_view(), name='cursos'),
   path('editar/<int:curso_id>/', CursoEdicaoView.as_view(), name='editar_curso'),
   path('excluir/<int:curso_id>/', CursoExclusaoView.as_view(), name='excluir_curso'),
]