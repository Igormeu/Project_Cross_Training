from flask import jsonify, request
from app.model.alunos import Aluno
from app import db
from datetime import datetime

def criar_aluno():
    data = request.json
    try:
        aluno = Aluno(
            nome = data['nome'],
            endereco = data['endereco'],
            cidade = data['cidade'],
            estado = data['estado'],
            telefone = data['telefone'],
            status = data.get('status', 'Cadastrado'),
            data_matricula = datetime.strptime(data['data_matricula'], "%Y-%m-%d") if data.get('data_matricula') else None,
            data_vencimento = datetime.strptime(data['data_vencimento'], "%Y-%m-%d") if data.get('data_vencimento') else None,
            data_desligamento = datetime.strptime(data['data_desligamento'], "%Y-%m-%d") if data.get('data_desligamento') else None
        )
        db.session.add(aluno)
        db.session.commit()
        return jsonify({'mensagem': 'Aluno criado com sucesso!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'erro': str(e)}), 400

def listar_alunos():
    alunos = Aluno.query.all()
    resultado = [a.serializeJSON() for a in alunos]
    return jsonify(resultado), 200

def atualizar_aluno(id):
    aluno = Aluno.query.get(id)
    if not aluno:
        return jsonify({'erro': 'Aluno não encontrado'}), 404
    
    data = request.json
    try:
        aluno.nome = data.get('nome', aluno.nome)
        aluno.endereco = data.get('endereco', aluno.endereco)
        aluno.cidade = data.get('cidade', aluno.cidade)
        aluno.estado = data.get('estado', aluno.estado)
        aluno.telefone = data.get('telefone', aluno.telefone)
        aluno.status = data.get('status', aluno.status)
        db.session.commit()
        return jsonify({'mensagem': 'Aluno atualizado com sucesso'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'erro': str(e)}), 400

def desmatricular_aluno(id):
    aluno = Aluno.query.get(id)
    if not aluno:
        return jsonify({'erro': 'Aluno não encontrado'}), 404
    elif aluno.status == 'Desligado' or aluno.data_desligamento is not None:
        return jsonify({'erro': 'Aluno já está desligado.'}), 400
    elif aluno.data_matricula is None:
        return jsonify({'erro': 'Aluno não possui matrícula ativa para ser desligado.'}), 400
    try:
        aluno.data_desligamento = datetime.now().date()
        aluno.data_matricula = None
        aluno.data_vencimento = None
        aluno.status = "Desligado"
        db.session.commit()
        return jsonify({'mensagem': 'Aluno desligado com sucesso'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'erro': str(e)}), 400

def deletar_aluno(id):
    aluno = Aluno.query.get(id)
    if not aluno:
        return jsonify({'erro': 'Aluno não encontrado'}), 404
    elif aluno.status != 'Desligado':
        return jsonify({'erro': 'Aluno ainda está ativo. Desligue o aluno antes de deletar.'}), 400
    try:
        db.session.delete(aluno)
        db.session.commit()
        return jsonify({'mensagem': 'Aluno deletado com sucesso'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'erro': str(e)}), 400