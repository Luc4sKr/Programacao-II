from config.configs import *
from models.pessoa import Pessoa

# curl localhost:5000/incluir_pessoa -X POST -d '{"nome":"john", "email":"jo@gmail.com"}' -H "Content-Type:application/json"
@app.route("/incluir_pessoa", methods=['POST'])
def incluir():
    dados = request.get_json()
    try:
        # cria a pessoa
        nova = Pessoa(**dados)
        
        # realiza a persistência da nova pessoa
        db.session.add(nova)
        db.session.commit()
        
        return jsonify({"resultado": "ok", "detalhes": "ok"})
    except Exception as e:
        return jsonify({"resultado": "erro", "detalhes": str(e)})