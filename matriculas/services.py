from .models import Matricula
from alunos.models import Aluno
from cursos.models import Curso

class MatriculaService:
    @staticmethod
    def listar_matriculas():
        return Matricula.objects.all()
    
    def adicionar_matricula(self, aluno_id, curso_id, status, data_matricula):
        try:
            aluno = Aluno.objects.get(id=aluno_id)
            curso = Curso.objects.get(id=curso_id)
            matricula = Matricula(aluno=aluno, curso=curso, status=status, data_matricula=data_matricula)
            matricula.save()
            return matricula
        except (Aluno.DoesNotExist, Curso.DoesNotExist):
            return None
    
    def listar_matriculas_ativas(self):
        return Matricula.objects.filter(status=True)
    
    def listar_matriculas_inativas(self):
        return Matricula.objects.filter(status=False)

    def editar_matricula(self, matricula_id, aluno, curso, data_matricula, status):
        try:
            matricula = Matricula.objects.get(id=matricula_id)

       
            aluno_instance = Aluno.objects.get(id=aluno)
            curso_instance = Curso.objects.get(id=curso)

           
            matricula.aluno = aluno_instance 
            matricula.curso = curso_instance
            
        
            matricula.status = status
            matricula.data_matricula = data_matricula
            matricula.save()
            return matricula
        except Matricula.DoesNotExist:
            return None
        
    def obter_matricula(self, matricula_id):
        try:
            return Matricula.objects.get(id=matricula_id)
        except Matricula.DoesNotExist:
            return None
        
    def excluir_matricula(self, matricula_id):
        try:
            matricula = Matricula.objects.get(id=matricula_id)
            matricula.delete()
            return True
        except Matricula.DoesNotExist:
            return False