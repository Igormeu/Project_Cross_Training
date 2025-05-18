from app import db

class Aluno (db.Model):
    __tablename__ = "alunos"
    __table_args__ = {'sqlite_autoincrement':True}

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable= True)
    endereco = db.Column(db.String(255), nullable = True)
    cidade = db.Column(db.String(50), nullable = True)
    estado = db.Column(db.String(2), nullable = True)
    telefone = db.Column(db.String(15), nullable = True, unique=True)
    status = db.Column(db.String(40), nullable = True, default='cadastrado')
    data_matricula = db.Column(db.Date, nullable = False)
    data_vencimento = db.Column(db.Date, nullable = False)
    data_desligamento = db.Column(db.Date, nullable = False)