from flask import jsonify, request
from app.model.alunos import Aluno
from app.model.pagamentos import Pagamento
from app import db
from datetime import datetime, timedelta

def criar_pagamento(id):
    try:
        aluno = Aluno.query.get(id)

        if not aluno:
            return jsonify({'erro': 'Aluno não encontrado'}), 404
        
        dados = request.json
        data_pagamento = datetime.today().date()
        
        if not dados.get('valor') or not dados.get('tipo'):
            return jsonify({'erro': 'Digite os campos de tipo e valor'})

        if dados.get('tipo') not in ['Cartão', 'Dinheiro']:
            return jsonify({'erro': 'Tipo inválido de pagamento'})
        
        try:
            valor = float(dados['valor'])
        except ValueError:
            return jsonify({'erro': 'Digite um valor de pagamento válido'}), 400
           
        novo_pagamento = Pagamento(
            aluno_id=id,
            data_pagamento = data_pagamento,
            valor=dados['valor'],
            tipo=dados['tipo']
        )

        db.session.add(novo_pagamento)

        if not aluno.data_matricula:
            data_matricula = data_pagamento
            if not aluno.data_vencimento:
                data_vencimento_novo = data_pagamento + timedelta(days=30)
            else:
                data_vencimento_novo = aluno.data_vencimento + timedelta(days=30)
        else:
            data_matricula = aluno.data_matricula
            data_vencimento_novo = aluno.data_vencimento + timedelta(days=30)

        aluno.status = 'matriculado'
        aluno.data_matricula = data_matricula
        aluno.data_vencimento = data_vencimento_novo
        aluno.data_desligamento = None
        db.session.commit()
        return jsonify({'mensagem': 'Pagamento criado com sucesso'}), 201

    except Exception as e:
         db.session.rollback()
         return jsonify({'erro': str(e)}), 400

def listar_pagamentos(id):
    try:
        aluno = Aluno.query.get(id)
        pagamentos = Pagamento.query.filter_by(aluno_id=id).all()

        if not aluno:
            return jsonify({'erro': 'Aluno não encontrado'}), 404
        
        resultado = []
        for pagamento in pagamentos:
            resultado.append({
                'id_pagamentos': pagamento.id_pagamentos,
                'valor': pagamento.valor,
                'tipo': pagamento.tipo,
                'data_pagamento': pagamento.data_pagamento.strftime("%Y-%m-%d")
            })
        
        if not resultado:
            return jsonify({'erro': 'Nenhum pagamento foi realizado pelo aluno'}), 404

        return jsonify(resultado)
    
    except Exception as e:
         db.session.rollback()
         return jsonify({'erro': str(e)}), 400

def atualizar_pagamento(id_pagamento):
    try:
        pagamento = Pagamento.query.get(id_pagamento)

        if not pagamento:
            return jsonify({'erro': 'Pagamento nao encontrado'}), 404

        dados = request.json

        if not dados.get('valor') or not dados.get('tipo'):
            return jsonify({'erro': 'Digite os campos de tipo e valor'})

        if dados.get('tipo') not in ['Cartão', 'Dinheiro']:
            return jsonify({'erro': 'Tipo inválido de pagamento'})
        
        try:
            valor = float(dados['valor'])
        except ValueError:
            return jsonify({'erro': 'Digite um valor de pagamento válido'}), 400
        
        pagamento.valor = dados['valor']
        pagamento.tipo = dados['tipo']
        db.session.commit()
        return jsonify({'mensagem': 'Pagamento atualizado com sucesso'}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'erro': str(e)}), 400
    

def deletar_pagamento(id_pagamento):
    try:
        pagamento = Pagamento.query.get(id_pagamento)

        if not pagamento:
            return jsonify({'erro': 'Pagamento nao encontrado'}), 404
        
        db.session.delete(pagamento)
        db.session.commit()
        return jsonify({'mensagem': 'Pagamento deletado com sucesso'}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'erro': str(e)}), 400
    


