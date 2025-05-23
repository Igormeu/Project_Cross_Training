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
    status = db.Column(db.String(40), nullable = False, default='ativo')
    data_matricula = db.Column(db.Date, nullable = True)
    data_vencimento = db.Column(db.Date, nullable = True)
    data_desligamento = db.Column(db.Date, nullable = True)

def __init__(self, nome, endereco, cidade, estado, telefone, status=None, dataMatricula=None, dataVencimento=None, desligamento=None):
    self.nome = nome
    self.endereco = endereco
    self.cidade = cidade
    self.estado = estado
    self.telefone = telefone
    self.status = status or 'ativo'
    self.data_matricula = dataMatricula
    self.data_vencimento = dataVencimento
    self.data_desligamento = desligamento
    
def cadastrarAluno(self, nome, endereco, cidade, estado, telefone):
    try:
        pass
        
    except Exception as error:
        print('Erro ao cadastrar novo aluno', error)

def listarAlunos(self, id):
    try:
        db.session.query(Aluno).filter(Aluno.id == id).all()
        alunos = [{}]
        return alunos
        
    except Exception as error:
        print('Erro ao listar os alunos', error)

def editarAluno(self, id): # Incluir parâmetros
    try:
        db.session.query(Aluno).filter(Aluno.id == id).update({})
        db.session.commit()
        
    except Exception as error:
        print('Erro ao editar aluno', error)

def excluirAluno(self, id):
    try:
        # Incluir verificação: excluir somente se status == 'inativo'
        db.session.query(Aluno).filter(Aluno.id == id).delete()
        db.session.commit()
        
    except Exception as error:
        print('Erro ao excluir aluno', error)
