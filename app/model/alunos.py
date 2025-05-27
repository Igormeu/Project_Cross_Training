from app import db
from datetime import datetime

class Aluno(db.Model):
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

    def desligarAluno(self): # atualização de status para total desligamento de aluno
        self.data_desligamento = datetime.now().date()
        self.status = "Desligado"
    
    def deletarAluno(self):
        from app import db
        db.session.delete(self)

    def checarStatus(self): # checagem de status de matrícula do usuário registrado
        hoje = datetime.now().date()
        return self.data_desligamento is None and (self.data_vencimento is None or hoje <= self.data_vencimento)

    def serializeJSON(self): # checa dados para retornar como JSON no view
        return {
            'id': self.id,
            'nome': self.nome,
            'endereco': self.endereco,
            'cidade': self.cidade,
            'estado': self.estado,
            'telefone': self.telefone,
            'status': self.status,
            'data_matricula': self.data_matricula.strftime('%Y-%m-%d') if self.data_matricula else None,
            'data_vencimento': self.data_vencimento.strftime('%Y-%m-%d') if self.data_vencimento else None,
            'data_desligamento': self.data_desligamento.strftime('%Y-%m-%d') if self.data_desligamento else None
        }