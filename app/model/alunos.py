from app import db
from datetime import datetime

class Aluno(db.Model):
    __tablename__ = "alunos"
    __table_args__ = {'sqlite_autoincrement':True}
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    endereco = db.Column(db.String(100))
    cidade = db.Column(db.String(100))
    estado = db.Column(db.String(2))
    telefone = db.Column(db.String(20))
    status = db.Column(db.String(20), default="Cadastrado")
    data_matricula = db.Column(db.Date, nullable=True)
    data_vencimento = db.Column(db.Date, nullable=True)
    data_desligamento = db.Column(db.Date, nullable=True)

    def checarStatus(self): # checagem de status de matrícula do usuário registrado
        hoje = datetime.now().date()
        return self.data_desligamento is None and (self.data_vencimento is None or hoje <= self.data_vencimento)