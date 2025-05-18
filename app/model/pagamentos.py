from app import db
from app.model.alunos import Aluno

class Pagamento (db.Model):
    __tablename__ = "pagamentos"
    __table_args__ = {'sqlite_autoincrement':True}

    id_pagamentos = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Float, nullable= True)
    tipo =  db.Column(db.String(10), nullable = True)
    data_pagamento = db.Column(db.Date, nullable= True)

    aluno_id = db.Column(db.Integer, db.ForeignKey('alunos.id'), nullable= True)
    aluno = db.relationship("Aluno", backref="pagamentos")