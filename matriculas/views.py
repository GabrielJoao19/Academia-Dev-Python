from django.shortcuts import render, redirect
from django.views import View
from .services import MatriculaService
from alunos.services import AlunoService
from cursos.services import CursoService


class MatriculasVIEW(View):
    def get(self, request):
        srv = MatriculaService()
        srv_alunos = AlunoService()
        srv_cursos = CursoService()
        alunos = srv_alunos.listar_alunos()
        cursos = srv_cursos.listar_cursos()
        matriculas = srv.listar_matriculas()
        contexto = {
            'alunos': alunos,
            'cursos': cursos,
            'matriculas': matriculas,
        }
        return render(request, 'lista_matriculas.html', contexto)
    
    def post(self, request):
        srv = MatriculaService()
        aluno = request.POST.get('aluno')
        curso = request.POST.get('curso')
        data_matricula = request.POST.get('data_matricula')
        status = request.POST.get('status')
        matricula_adicionado = srv.adicionar_matricula(aluno, curso, status, data_matricula)
        return redirect('matriculas:matriculas')
    
class MatriculaEdicaoView(View):
    def get(self, request, matricula_id):
        srv = MatriculaService()
        srv_alunos = AlunoService()
        srv_cursos = CursoService()
        alunos = srv_alunos.listar_alunos()
        cursos = srv_cursos.listar_cursos()
        matricula = srv.obter_matricula(matricula_id)
        contexto = {
            'alunos': alunos,
            'cursos': cursos,
            'matricula': matricula,
        }
        if matricula:
            return render(request, 'editar_matricula.html', contexto)
 
    def post(self, request, matricula_id):
        srv = MatriculaService()
        matricula_editada = srv.editar_matricula(
            matricula_id,
            aluno=request.POST.get('aluno'),
            curso=request.POST.get('curso'),
            data_matricula=request.POST.get('data_matricula'),
            status=request.POST.get('status')
        )
        if matricula_editada:
            return redirect('matriculas:matriculas')
        
class MatriculaExclusaoView(View):
    def post(self, request, matricula_id):
        srv = MatriculaService()
        sucesso = srv.excluir_matricula(matricula_id)
        return redirect('matriculas:matriculas')