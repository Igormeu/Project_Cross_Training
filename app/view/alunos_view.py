#Rotas da Entidade Aluno

from flask import render_template
from app import enviroment

#teste
@enviroment.route('/aluno')
def aluno():
    return '<h1> Alunos </h1>'
