from flask import Blueprint
from app.view import alunos_view

aluno_bp = Blueprint('alunos', __name__)

#@aluno_bp.route('/alunos', methods=['POST'])
#def criar_alunos:
#  return alunos_view.criar_aluno
aluno_bp.route('/alunos', methods=['POST'])(alunos_view.criar_aluno)
aluno_bp.route('/alunos', methods=['GET'])(alunos_view.listar_alunos)
aluno_bp.route('/alunos/<int:id>', methods=['PUT'])(alunos_view.atualizar_aluno)
aluno_bp.route('/alunos/<int:id>', methods=['DELETE'])(alunos_view.deletar_aluno)
