from app import db
from app.model.alunos import Aluno

class Pagamento (db.Model):
    __tablename__ = "pagamentos"
    __table_args__ = {'sqlite_autoincrement':True}

    id_pagamentos = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Float, nullable= False)
    tipo =  db.Column(db.String(10), nullable = False)
    data_pagamento = db.Column(db.Date, nullable= False)

    aluno_id = db.Column(db.Integer, db.ForeignKey('alunos.id'), nullable= False)
    aluno = db.relationship("Aluno", backref="pagamentos")