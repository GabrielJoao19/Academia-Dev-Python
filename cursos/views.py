from django.shortcuts import render, redirect
from django.views import View
from .services import CursoService

class CursosVIEW(View):
    def get(self, request):
        srv = CursoService()
        cursos = srv.listar_cursos()
        return render(request, 'lista_cursos.html', {'cursos': cursos})
    
    def post(self, request):
        srv = CursoService()
        nome = request.POST.get('nome')
        carga_horaria = request.POST.get('carga_horaria')
        valor_inscricao = request.POST.get('valor_inscricao')
        status = request.POST.get('status')
        curso_adicionado = srv.adicionar_curso(nome, carga_horaria, valor_inscricao, status)
        return redirect('cursos:cursos')
    
class CursoEdicaoView(View):
    def get(self, request, curso_id):
        srv = CursoService()
        nome = request.GET.get('nome')
        carga_horaria = request.GET.get('carga_horaria')
        valor_inscricao = request.GET.get('valor_inscricao')
        status = request.GET.get('status')
        curso = srv.editar_curso(curso_id, nome, carga_horaria, valor_inscricao, status)
        if curso:
            return render(request, 'editar_curso.html', {'curso': curso})
        else:
            return redirect('cursos:cursos')
        
    def post(self, request, curso_id):
        srv = CursoService()
        nome = request.POST.get('nome')
        carga_horaria = request.POST.get('carga_horaria')
        valor_inscricao = request.POST.get('valor_inscricao')
        status = request.POST.get('status')
        curso = srv.editar_curso(curso_id, nome, carga_horaria, valor_inscricao, status)
        if curso:
            return redirect('cursos:cursos')
        else:
            return redirect('cursos:cursos')
        
class CursoExclusaoView(View):
    def post(self, request, curso_id):
        srv = CursoService()
        sucesso = srv.excluir_curso(curso_id)
        return redirect('cursos:cursos')

