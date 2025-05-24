from app import db
from sqlalchemy.exc import IntegrityError, OperationalError, SQLAlchemyError

class Aluno (db.Model):
    __tablename__ = "alunos"
    __table_args__ = {'sqlite_autoincrement':True}

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable= False)
    endereco = db.Column(db.String(255), nullable = False)
    cidade = db.Column(db.String(50), nullable = False)
    estado = db.Column(db.String(2), nullable = False)
    telefone = db.Column(db.String(15), nullable = False, unique=True)
    status = db.Column(db.String(40), nullable = False, default='Cadastrado(a)')
    data_matricula = db.Column(db.Date, nullable = True)
    data_vencimento = db.Column(db.Date, nullable = True)
    data_desligamento = db.Column(db.Date, nullable = True)

    def __init__ (self, nome, endereco, cidade, estado, telefone, status, data_matricula, data_vencimento, data_desligamento):
        self.nome = nome
        self.endereco = endereco
        self.cidade = cidade
        self.estado = estado
        self.telefone = telefone
        self.status = status
        self.data_matricula = data_matricula
        self.data_vencimento = data_vencimento
        self.data_desligamento = data_desligamento
    
    def cadastrarAluno(self, nome, endereco, cidade, estado, telefone, data_matricula, data_vencimento):
        try:
            insert_db = Aluno(nome, endereco, cidade, estado, telefone, data_matricula, data_vencimento)
            db.session.add(insert_db)
            db.session.commit()

        except IntegrityError:
            db.session.rollback() # desfaz a operação para o SQLAlchemy prosseguir normalmente o 'try'
            print("Erro de integridade. Verifique se os dados estão corretos.")

        except OperationalError:
            db.session.rollback()
            print("Erro operacional. Verifique a conexão com o banco.")

        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Erro inesperado: {e}")

    def alunoStatus(self):
        if self.data_desligamento is None and self.data_matricula <= self.data_vencimento:
            db.session.query(Aluno).filter(Aluno).update({"status": 'Cadastrado(a)'})
            db.session.commit()
        elif self.data_desligamento > self.data_matricula:
            db.session.query(Aluno).filter(Aluno).update({"status": 'Não Cadastrado(a)'})
            db.session.commit()
        else:
            db.session.query(Aluno).filter(Aluno).update({"status": None})
            db.session.commit()
        # verifica se a pessoa é ou não um aluno e atualiza seu status
    
    def atualizarAluno(self, id, nome, endereco, cidade, estado, telefone, data_matricula, data_vencimento, data_desligamento):
        try:
            db.session.query(Aluno).filter(Aluno.id == id).update({
            "id": id,
            "nome": nome,
            "endereco": endereco,
            "cidade": cidade,
            "estado": estado,
            "telefone": telefone,
            "data_matricula": data_matricula,
            "data_vencimento": data_vencimento,
            "data_desligamento": data_desligamento
            })
            db.session.commit()

        except IntegrityError:
            db.session.rollback()
            print("Erro de integridade. Verifique se os dados estão corretos.")

        except OperationalError:
            db.session.rollback()
            print("Erro operacional. Verifique a conexão com o banco.")

        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Erro inesperado: {e}")
        
    def deletarAluno(self, id, data_desligamento):
        try:
            db.session.query(Aluno).filter(Aluno.id == id and data_desligamento > self.data_matricula).update({
                "data_desligamento": data_desligamento, "data_matricula": None, "data_vencimento": None
                })

        except OperationalError:
            db.session.rollback()
            print("Erro operacional. Verifique a conexão com o banco.")

        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Erro inesperado: {e}")