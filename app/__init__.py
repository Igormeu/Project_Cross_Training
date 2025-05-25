from flask import Flask
from flask_sqlalchemy import SQLAlchemy

enviroment = Flask(__name__) 
#Definir URI do banco de dados
enviroment.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///crud.db"
enviroment.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(enviroment)

from app.routes.alunos_rotas import aluno_bp
enviroment.register_blueprint(aluno_bp)


