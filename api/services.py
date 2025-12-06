from alunos.models import Aluno
from matriculas.models import Matricula
from cursos.models import Curso

class AcademiaService:
    def total_matriculas_por_curso(self):
        cursos = Curso.objects.all()
        total_matriculas = {}
        for curso in cursos:
            total = Matricula.objects.filter(curso=curso).count()
            total_matriculas[curso.nome] = total
        return total_matriculas
    
    def total_devido_por_aluno(self, aluno_id):
        try:
            aluno = Aluno.objects.get(id=aluno_id)
            matriculas = Matricula.objects.filter(aluno=aluno, status=False).select_related('curso')
            total_devido = sum(matricula.curso.valor_inscricao for matricula in matriculas)
            return total_devido
        except Aluno.DoesNotExist:
            return 0
        
    def totat_pagamentos_pendentes(self):
        matriculas_pendentes = Matricula.objects.filter(status=False).select_related('aluno', 'curso')
        total_pendente = sum(matricula.curso.valor_inscricao for matricula in matriculas_pendentes)
        return total_pendente