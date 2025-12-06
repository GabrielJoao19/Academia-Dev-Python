from alunos.models import Aluno
from matriculas.models import Matricula

class FinanceiroService:
    def total_pago_por_aluno(self,aluno_id):
        try:
            aluno = Aluno.objects.get(id=aluno_id)
            matriculas = Matricula.objects.filter(aluno=aluno, status=True).select_related('curso')
            total_pago = sum(matricula.curso.valor_inscricao for matricula in matriculas)
            return total_pago    
        except Aluno.DoesNotExist:
            return 0
        
    def total_devido_por_aluno(self, aluno_id):
        try:
            aluno = Aluno.objects.get(id=aluno_id)
            matriculas = Matricula.objects.filter(aluno=aluno, status=False).select_related('curso')
            total_devido = sum(matricula.curso.valor_inscricao for matricula in matriculas)
            return total_devido
            
        except Aluno.DoesNotExist:
            return 0