from django.shortcuts import render
from django.views import View
from alunos.services import AlunoService
from matriculas.services import MatriculaService
from cursos.services import CursoService
# Create your views here.

class DashboardVIEW(View):
    def get(self, request):
        srv_alunos = AlunoService()
        srv_matriculas = MatriculaService()
        srv_cursos = CursoService()
        alunos = srv_alunos.contar_alunos()
        cursos = srv_cursos.listar_cursos_ativos()
        matriculas_ativas = srv_matriculas.listar_matriculas_ativas()
        matriculas_inativas = srv_matriculas.listar_matriculas_inativas()
        dados = {
            'total_alunos': alunos,
            'total_cursos_ativos': cursos,
            'matriculas_ativas': matriculas_ativas,
            'matriculas_inativas': matriculas_inativas,
        }
        return render(request, 'dashboard.html', dados)