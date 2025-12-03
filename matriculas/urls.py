from django.urls import path
from .views import MatriculaAPIView, MatriculasAPIView

app_name = 'matriculas'

urlpatterns = [
    path('matriculas/', MatriculasAPIView.as_view(), name='matriculas'),
    path('matriculas/<int:pk>/', MatriculaAPIView.as_view(), name='matricula'),
]

