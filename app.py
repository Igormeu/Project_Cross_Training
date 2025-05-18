from app import enviroment, db
from app.model.alunos import Aluno
from app.model.pagamentos import Pagamento

with enviroment.app_context():
    db.create_all()

if __name__ == "__main__":
    enviroment.run(debug=True, host="127.0.0.1", port="8080")