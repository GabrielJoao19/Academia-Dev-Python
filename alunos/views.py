from django.shortcuts import render, redirect
from django.views import View
from .services import AlunoService
from matriculas.services import MatriculaService

class AlunosVIEW(View):
    def get(self, request):
        srv = AlunoService()
        srv_matriculas = MatriculaService()
        matriculas = srv_matriculas.listar_matriculas()
        alunos = srv.listar_alunos()
        contexto = {
            'alunos': alunos,
            'matriculas': matriculas,
        }
        return render(request, 'lista_alunos.html', contexto)
    
    def post(self, request):
        srv = AlunoService()
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        data_ingresso = request.POST.get('data_ingresso')
        aluno_adicionado = srv.adicionar_aluno(nome, email, cpf, data_ingresso)
        return redirect('alunos:alunos')

class AlunoEdicaoView(View):
    def get(self, request, aluno_id):
        srv = AlunoService()
        nome = request.GET.get('nome')
        email = request.GET.get('email')
        cpf = request.GET.get('cpf')
        data_ingresso = request.GET.get('data_ingresso')
        aluno = srv.editar_aluno(aluno_id, nome, email, cpf, data_ingresso)
        if aluno:
            return render(request, 'editar_aluno.html', {'aluno': aluno})
        else:
            return redirect('alunos:alunos')
        
    def post(self, request, aluno_id):
        srv = AlunoService()
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        data_ingresso = request.POST.get('data_ingresso')
        aluno = srv.editar_aluno(aluno_id, nome, email, cpf, data_ingresso)
        if aluno:
            return redirect('alunos:alunos')
        else:
            return redirect('alunos:alunos')
        
class AlunoExclusaoView(View):
    def post(self, request, aluno_id):
        srv = AlunoService()
        sucesso = srv.excluir_aluno(aluno_id)
        return redirect('alunos:alunos')
    
class AlunosPagamentoView(View):
    def get(self, request, aluno_id):
        srv = AlunoService()
        total_pago = srv.pago_por_aluno_otimizado(aluno_id)
        return render(request, 'pagamento_aluno.html', {'total_pago': total_pago})

        
