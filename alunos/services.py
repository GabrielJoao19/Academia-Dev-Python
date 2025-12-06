from .models import Aluno
from matriculas.models import Matricula
class AlunoService:
    @staticmethod
    def listar_alunos():
        return Aluno.objects.all()
    
    def pegar_aluno(self, aluno_id):
        try:
            return Aluno.objects.get(id=aluno_id)
        except Aluno.DoesNotExist:
            return None
    
    def adicionar_aluno(self, nome, email, cpf, data_ingresso):
        aluno = Aluno(nome=nome, email=email, cpf=cpf, data_ingresso=data_ingresso)
        aluno.save()
        return aluno
    
    def contar_alunos(self):
        return Aluno.objects.count()

    def editar_aluno(self, aluno_id, nome, email, cpf, data_ingresso):
        try:
            aluno = Aluno.objects.get(id=aluno_id)
            if nome:
                aluno.nome = nome
            if email:
                aluno.email = email
            if cpf:
                aluno.cpf = cpf
            if data_ingresso:
                aluno.data_ingresso = data_ingresso
            aluno.save()
            return aluno
        except Aluno.DoesNotExist:
            return None
        
    def excluir_aluno(self, aluno_id):
        try:
            aluno = Aluno.objects.get(id=aluno_id)
            aluno.delete()
            return True
        except Aluno.DoesNotExist:
            return False
        