from rest_framework import generics
from .models import Aluno
from .serializers import AlunoSerializer

class AlunosAPIView(generics.ListCreateAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class AlunoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer