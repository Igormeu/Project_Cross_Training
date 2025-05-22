#Rotas da Entidade Aluno

from flask import render_template, jsonify,request
from app import enviroment, db
from app.model.alunos import Aluno

#teste
@enviroment.route('/aluno')
def aluno():
    return '<h1> Alunos </h1>'

@enviroment.route('/lista_alunos', methods=['GET'])
def listarAlunos():
    listaAlunos = []

    try:
        alunos = Aluno.query.all()

        for aluno in alunos:
            dict_aluno = {
            'id': aluno.id,
            'nome': aluno.nome,
            'endereco': aluno.endereco,
            'cidade': aluno.cidade,
            'estado': aluno.estado,
            'telefone': aluno.telefone,
            'status': aluno.status,
            'data_matricula': aluno.data_matricula,
            'data_desligamento': aluno.data_desligamento,
            'data_vencimento': aluno.data_vencimento
            }
            listaAlunos.append(dict_aluno)

        if not listaAlunos:
            return ({"mensagem": "Não há registros de cadastro de alunos"})
        return jsonify(listaAlunos)

            
    except Exception as e:
        return jsonify({"mensagem": f"Erro ao acessar o Banco de Dados {e}"})





