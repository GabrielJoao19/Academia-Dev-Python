from django.urls import path
from .views import MatriculasVIEW, MatriculaEdicaoView, MatriculaExclusaoView
app_name = 'matriculas'
urlpatterns = [
    path('', MatriculasVIEW.as_view(), name='matriculas'),
    path('editar/<int:matricula_id>/', MatriculaEdicaoView.as_view(), name='editar_matricula'),
    path('excluir/<int:matricula_id>/', MatriculaExclusaoView.as_view(), name='excluir_matricula'),
]

