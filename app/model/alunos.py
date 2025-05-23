from app import db

class Aluno (db.Model):
    __tablename__ = "alunos"
    __table_args__ = {'sqlite_autoincrement':True}

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable= False)
    endereco = db.Column(db.String(255), nullable = False)
    cidade = db.Column(db.String(50), nullable = False)
    estado = db.Column(db.String(2), nullable = False)
    telefone = db.Column(db.String(15), nullable = False, unique=True)
    status = db.Column(db.String(40), nullable = False, default='cadastrado')
    data_matricula = db.Column(db.Date, nullable = True)
    data_vencimento = db.Column(db.Date, nullable = True)
    data_desligamento = db.Column(db.Date, nullable = True)

def __init__(self, nome, endereco, cidade, estado, telefone, status, matricula, vencimento, desligamento):
    self.nome = nome
    self.endereco = endereco
    self.cidade = cidade
    self.estado = estado
    self.telefone = telefone
    self.status = status
    self.data_matricula = matricula
    self.data_vencimento = vencimento
    self.data_desligamento = desligamento
    
def cadastrarAluno():
    pass

def listarAlunos():
    pass

def editarAluno():
    pass

def excluirAluno():
    pass