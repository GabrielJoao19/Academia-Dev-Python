from django.shortcuts import render
from django.views import View
from .services import FinanceiroService
from alunos.services import AlunoService
from matriculas.services import MatriculaService
# Create your views here.

class DashboardVIEW(View):
    def get(self, request):
        srv_aluno = AlunoService()
        srv = FinanceiroService()
        srv_matricula = MatriculaService()
        matriculas = srv_matricula.listar_matriculas()
        alunos = srv_aluno.listar_alunos()
        lista_aluno_financeiro = []
        for aluno in alunos:
            total_pago = srv.total_pago_por_aluno(aluno.id)
            total_devido = srv.total_devido_por_aluno(aluno.id)
            lista_aluno_financeiro.append({
                'aluno': aluno,
                'total_pago': total_pago,
                'total_devido': total_devido,
            })
        contexto = {
            'lista_aluno_financeiro': lista_aluno_financeiro,
            'matriculas': matriculas,
            'alunos': alunos,
        }
        return render(request, 'financeiro.html', contexto)
