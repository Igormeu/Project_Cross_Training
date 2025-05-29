from flask import Blueprint
from app.view import pagamentos_view

pagamento_bp = Blueprint('pagamentos', __name__)

pagamento_bp.route('/pagamentos/<int:id>', methods=['POST'])(pagamentos_view.criar_pagamento)
pagamento_bp.route('/pagamentos/<int:id>', methods=['GET'])(pagamentos_view.listar_pagamentos)
