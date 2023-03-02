from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime

from models.pessoa import *

app = Flask(__name__)

# aplicando tratamento CORS ao flask
# https://flask-cors.readthedocs.io/en/latest/
CORS(app)


@app.route("/")
def index():
    return "<h1>Index page</h1>"

# rota de listar pessoas
@app.route("/listar_pessoas")
def listar():
    lista_retorno = []
    
    lista = [
        Pessoa(nome="João da Silva",
               email="josilva@gmail.com",
               telefone="47 99012 3232",
               nascimento=datetime(1999, 12, 20)),
        Pessoa(nome="Maria Oliveira",
               email="maliva@gmail.com",
               telefone="47 98823 4321",
               nascimento=datetime(2001, 9, 11)),
        Pessoa(nome="Teresa Soares",
               email="teso@gmail.com",
               telefone="47 98114 1423",
               nascimento=datetime(1977, 12, 19)),
    ]
    
    [lista_retorno.append(p.json()) for p in lista]
    
    # retornar a lista de pessoas json1
    return jsonify(lista_retorno)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
