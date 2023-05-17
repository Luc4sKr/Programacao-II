from flask import Flask, jsonify, request
from flask_cors import CORS

from models.pessoa import Pessoa

app = Flask(__name__)
with app.app_context():
    CORS(app)

    @app.route("/")
    def index():
        return "operação post"

    # rota de listar pessoas
    @app.route("/incluir_pessoa", methods=['POST'])
    def incluir():
        # receber as informações da nova pessoa
        dados = request.get_json()
        try: 
            nova = Pessoa(**dados)

            return jsonify({"resultado":"ok"})
        except Exception as e:
            return jsonify({"resultado":"erro"})
    
if __name__ == "__main__":
    app.run(debug=True)
