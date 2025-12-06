from .models import Curso

class CursoService:
    @staticmethod
    def listar_cursos():
        return Curso.objects.all()
    
    def listar_cursos_ativos(self):
        return Curso.objects.filter(status=True)
    
    def adicionar_curso(self, nome, carga_horaria, valor_incscricao, status=True):
        curso = Curso(nome=nome, carga_horaria=carga_horaria, valor_inscricao=valor_incscricao, status=status)
        curso.save()
        return curso
    
    def editar_curso(self, curso_id, nome=None, carga_horaria=None, valor_inscricao=None, status=None):
        try:
            curso = Curso.objects.get(id=curso_id)
            if nome:
                curso.nome = nome
            if carga_horaria:
                curso.carga_horaria = carga_horaria
            if valor_inscricao:
                curso.valor_inscricao = valor_inscricao
            if status is not None:
                curso.status = status
            curso.save()
            return curso
        except Curso.DoesNotExist:
            return None
        
    def excluir_curso(self, curso_id):
        try:
            curso = Curso.objects.get(id=curso_id)
            curso.delete()
            return True
        except Curso.DoesNotExist:
            return False