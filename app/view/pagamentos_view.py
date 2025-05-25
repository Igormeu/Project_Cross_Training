#Rotas da Entidade Pagamento

from flask import render_template
from app import enviroment

#teste
@enviroment.route('/pagamento')
def pagamento():
    return '<h1> Pagamentos </h1>'