## Sobre o Projeto

O Projeto **Academia** é um sistema de gerenciamento de dados de alunos, cursos, matrículas e finanças, desenvolvido com **Django** e **Django REST Framework (DRF)**.

A aplicação é totalmente **Dockerizada**, utilizando **Docker Compose** para orquestrar o servidor web (Django) e o banco de dados **PostgreSQL**, garantindo um ambiente de desenvolvimento isolado e pronto para uso.

---

## Tecnologias Principais

* **Backend:** Python e Django 4.x
* **Banco de Dados:** PostgreSQL
* **Containerização:** Docker & Docker Compose

---

## Guia de Inicialização Rápida

O ambiente está configurado para ser iniciado com um único comando, usando o **Docker Compose**.

### Pré-requisitos

Certifique-se de ter o **Docker** instalado e em execução.

### 1. Clonar o Repositório

```bash
git clone [https://www.youtube.com/watch?v=X49Wz3icO3E](https://www.youtube.com/watch?v=X49Wz3icO3E)
cd [NOME DA PASTA DO PROJETO]
```

### 2. Iniciar a Aplicação (Build e Run)

O comando a seguir irá construir a imagem do serviço `web` e iniciar todos os contêineres (`web` e `db`). O *entrypoint* do serviço `web` executa as migrações automaticamente na primeira inicialização.

```bash
docker-compose up --build
```

####  Após isso, o avaliador deve acessar:
```bash
http://localhost:8000 (frontend)
http://localhost:8000/api/... (endpoints DRF)
```

## 💻 Documentação dos Endpoints da API

### I. Gerenciamento de Entidades (CRUD Básico)

Estes *endpoints* são usados para **criar, ler, atualizar e deletar (CRUD)** as entidades principais do sistema (Alunos, Cursos e Matrículas).

#### Alunos 

* `/alunos/` (`GET`, `POST`): Lista todos os alunos ou permite criar um **novo aluno**.
* `/alunos/<int:pk>/` (`GET`, `PUT`, `DELETE`): Permite recuperar, atualizar ou deletar um **aluno específico** pelo ID (`pk`).

#### Cursos 

* `/cursos/` (`GET`, `POST`): Lista todos os cursos ou permite criar um **novo curso**.
* `/cursos/<int:pk>/` (`GET`, `PUT`, `DELETE`): Permite recuperar, atualizar ou deletar um **curso específico** pelo ID (`pk`).

#### Matrículas (Geral) 

* `/matriculas/` (`GET`, `POST`): Lista todas as matrículas ou permite criar uma **nova matrícula**.
* `/matriculas/<int:pk>/` (`GET`, `PUT`, `DELETE`): Permite recuperar, atualizar ou deletar uma **matrícula específica** pelo ID (`pk`).

#### Matrículas (Aninhadas por Aluno) 

* `/alunos/<int:aluno_pk>/matriculas` (`GET`, `POST`): Lista todas as matrículas de um **aluno específico**. Também permite criar uma nova matrícula para este aluno.
* `/alunos/<int:aluno_pk>/matriculas/<int:matricula_pk>/` (`GET`, `PUT`, `DELETE`): Permite acessar, editar ou deletar uma matrícula específica, garantindo que ela pertença ao aluno informado.

---

### II. Relatórios e Consultas Customizadas (Ações GET)

Estes *endpoints* realizam consultas complexas e retornam dados de relatórios, geralmente utilizando uma *ViewSet* customizada:

* **Matrículas por Curso:**
    * `/relatorios/matriculas-curso/`: Retorna o **total de matrículas agrupadas por curso**.
* **Dívida por Aluno:**
    * `/relatorios/devido-aluno/`: Calcula e retorna o **total devido por cada aluno** (relatório de situação financeira).
* **Pagamentos Pendentes:**
    * `/relatorios/pendentes/`: Lista todos os **pagamentos de mensalidades que estão pendentes**.
* **SQL Bruto de Dívidas:**
    * `/relatorios/sql-bruto-devido/`: Retorna um **relatório de dívidas** gerado usando uma consulta SQL "bruta" customizada.