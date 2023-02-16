from flask import Flask, render_template, jsonify
import json

from models.pessoa import Pessoa

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/listar_pessoas")
def listar_pessoas():
    lista = list()

    p1 = Pessoa(id=1, nome="Lucas", idade=17)

    lista.append(p1.json())

    return jsonify(lista)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)