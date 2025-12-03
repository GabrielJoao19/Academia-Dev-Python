from rest_framework import generics
from .models import Matricula
from .serializers import MatriculaSerializer
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import action



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



   