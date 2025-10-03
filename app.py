from flask import Flask, render_template, request, redirect
from aluno_dao import AlunoDAO  
from professor_dao import ProfessorDAO  
from turma_dao import TurmaDAO  
from curso_dao import CursoDAO  

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


@app.route('/alunos') 
def listar_aluno():
    dao = AlunoDAO()
    lista_alunos = dao.listar()
    return render_template('aluno/listar.html', lista_alunos=lista_alunos)



# Rota para exibir o formulário
@app.route('/alunos/form') # rota formulario de aluno
def form_aluno():
    return render_template('aluno/form.html',aluno=None) # rederiza o arquivo formulario com aluno vazio


@app.route('/alunos/salvar/', methods=['POST'])  # Inserção
@app.route('/alunos/salvar/<int:id>', methods=['POST'])  # Atualização
def salvar_aluno(id=None):
    nome = request.form['nome']
    idade = request.form['idade']
    cidade = request.form['cidade']

    dao = AlunoDAO()
    resultado = dao.salvar(id, nome, idade, cidade) 

    if resultado["status"] == "ok":
        return redirect('/alunos')
    else:
        return f"<h2>{resultado['mensagem']}</h2><a href='/alunos'>Voltar</a>"

@app.route('/alunos/editar/<int:id>')
def editar_aluno(id):
    dao = AlunoDAO()
    aluno = dao.buscar_por_id(id)
    return render_template('aluno/form.html', aluno=aluno)


@app.route("/alunos/remover/<int:id>")
def remover_aluno(id):
    dao = AlunoDAO()
    resultado = dao.remover(id)
    if resultado["status"] == "ok":
       return redirect('/alunos')
    else:
        return f"Erro ao remover: {resultado['mensagem']}"
    

@app.route('/professor') 
def listar_professor():
    dao = ProfessorDAO()
    lista_professor = dao.listar()
    return render_template('professor/listar.html', lista_professor=lista_professor)

# Rota para exibir o formulário
@app.route('/professor/form') # rota formulario de aluno
def form_professor():
    return render_template('professor/form.html',professor=None) # rederiza o arquivo formulario com aluno vazio


@app.route('/professor/salvar/', methods=['POST'])  # Inserção
@app.route('/professor/salvar/<int:id>', methods=['POST'])  # Atualização
def salvar_professor(id=None):
    nome = request.form['nome']
    disciplina = request.form['disciplina']

    dao = ProfessorDAO()
    resultado = dao.salvar(id, nome, disciplina) 

    if resultado["status"] == "ok":
        return redirect('/professor')
    else:
        return f"<h2>{resultado['mensagem']}</h2><a href='/alunos'>Voltar</a>"



@app.route('/turma')
def listar_turma():
    dao = TurmaDAO()
    lista_turma = dao.listar()
    return render_template('turma/listar.html', lista_turma=lista_turma)

@app.route('/turma/form') 
def form_turma():
    lista_professores = ProfessorDAO().listar()
    lista_cursos = CursoDAO().listar()
    return render_template('turma/form.html',
                           turma=None,
                           lista_professores=lista_professores,
                           lista_cursos=lista_cursos) 


@app.route('/turma/salvar/', methods=['POST'])
@app.route('/turma/salvar/<int:id>', methods=['POST'])
def salvar_turma(id=None):
    semestre = request.form['semestre']
    curso_id = request.form['curso_id']
    professor_id = request.form['professor_id']
    dao = TurmaDAO()
    resultado = dao.salvar(id, semestre, curso_id, professor_id)
    if resultado['status'] == 'ok':
        return redirect('/turma')
    else:
        return f"<h2>{resultado['mensagem']}</h2><a href='/turmas'>Voltar</a>"


@app.route('/turma/editar/<int:id>')
def editar_turma(id):
    lista_professores = ProfessorDAO().listar()
    lista_cursos = CursoDAO().listar()
    dao = TurmaDAO()
    turma = dao.buscar_por_id(id)
    return render_template('turma/form.html', 
                           turma=turma,
                           lista_professores=lista_professores,
                           lista_cursos=lista_cursos) 


@app.route("/turma/remover/<int:id>")
def remover_turma(id):
    dao = TurmaDAO()
    resultado = dao.remover(id)
    if resultado["status"] == "ok":
       return redirect('/turma')
    else:
        return f"Erro ao remover: {resultado['mensagem']}"




@app.route('/teste') 
def teste():
    dao = AlunoDAO()
    lista_alunos = dao.listar()
    lista_cursos = CursoDAO().listar()
    return render_template('aluno/teste.html', 
                           lista_alunos=lista_alunos,
                           lista_cursos=lista_cursos)
    
    
@app.route('/receber_teste/', methods=['POST'])  # Atualização
def receber_teste(id=None):
    curso_id = request.form['curso_id']
    return f"<h2>ID recebido: {curso_id} </h2><a href='/teste'>Voltar</a>"



    
if __name__ == '__main__':
    app.run(debug=True)
   
    
    