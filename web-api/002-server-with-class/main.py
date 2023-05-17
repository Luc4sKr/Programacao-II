from flask import Flask, jsonify

from models.pessoa import Pessoa

app = Flask(__name__)


@app.route("/")
def index():
    return """
            <h1>Index</h1>
            <a href="/list">Lista de pessoas</a>
            """


@app.route("/list")
def list():
    callback_list = []  # criar uma lista vazia para retorno das informações
    lista_pessoas = [
        Pessoa(nome="João da Silva",
               email="josilva@gmail.com",
               telefone="47 99012 3232"),
        Pessoa(nome="Maria Oliveira",
               email="maliva@gmail.com",
               telefone="47 98823 4321"),
        Pessoa(nome="Teresa Soares",
               email="teso@gmail.com",
               telefone="47 98114 1423"),
    ]

    for p in lista_pessoas:
        callback_list.append(p.json())

    return jsonify(callback_list)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
