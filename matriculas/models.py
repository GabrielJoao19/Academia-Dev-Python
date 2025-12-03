from django.db import models

class Matricula(models.Model):
    aluno = models.ForeignKey('alunos.Aluno', on_delete=models.CASCADE)
    curso = models.ForeignKey('cursos.Curso', on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    
    @property
    def status_descricao(self):
        return "Pago" if self.status else "Pendente"
