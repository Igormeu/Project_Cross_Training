from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
enviroment = Flask(__name__) 
#Definir URI do banco de dados
enviroment.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///crud.db"
enviroment.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(enviroment)


@enviroment.route("/") #Decorador python
def index ():
    return render_template("index.html")

@enviroment.route("/newRequest") #Decorador python
def request ():
    return "<h1> Say me what is your new request:  </h1>"
