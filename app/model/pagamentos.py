from app import db
from app.model.alunos import Aluno

class Pagamento (db.Model):
    __tablename__ = "pagamentos"
    __table_args__ = {'sqlite_autoincrement':True}

    id = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Float, nullable= False)
    tipo =  db.Column(db.String(10), nullable = False)
    data_pagamento = db.Column(db.Date, nullable= False)

    aluno_id = db.Column(db.Integer, db.ForeignKey('alunos.id'), nullable= False)
    aluno = db.relationship("Aluno", backref="pagamentos")
    
def __init__(self, valor, tipo, data_pagamento, aluno):
    self.valor = valor
    self.tipo = tipo
    self.data_pagamento = data_pagamento
    self.aluno_id = aluno
    
def novoPagamento(self, valor, tipo, data, alunoId):
    try:
        aluno = Aluno.query.get(alunoId)
        if aluno is None:
            raise ValueError(f'Aluno {alunoId} não encontrado')

        db.session.add(Pagamento(valor, tipo, data, aluno))
        db.session.commit()

    except Exception as error:
        db.session.rollback()
        print('Erro ao registrar pagamento', error)
    
def historicoPagamentos(self, aluno_id):
    try:
        pagamentos = db.session.query(Pagamento).filter(Pagamento.aluno_id == aluno_id).all()
        
        pagamentos_dict = []
        for pagamento in pagamentos:
            aluno_nome = pagamento.aluno.nome
            
            pagamentos_dict.append({
                'id': pagamento.id,
                'aluno': aluno_nome,
                'valor': pagamento.valor,
                'tipo': pagamento.tipo,
                'data': pagamento.data_pagamento
            })
        
        return pagamentos_dict
    
    except Exception as error:
        db.session.rollback()
        print("Erro ao visualizar o histórico de pagamentos:", error)