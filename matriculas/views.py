from rest_framework import generics
from .models import Matricula
from .serializers import MatriculaSerializer

class MatriculasAPIView(generics.ListCreateAPIView):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class MatriculaAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
