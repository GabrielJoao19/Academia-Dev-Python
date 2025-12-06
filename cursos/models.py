from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria = models.CharField(max_length=50)
    valor_inscricao = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
    
    @property
    def status_descricao(self):
        return "Ativo" if self.status else "Inativo"
    
