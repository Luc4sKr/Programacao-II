from config.configs import *
from models.celular import Celular

# curl localhost:5000/incluir_celular -X POST -d '{"marca":"Xiomi", "modelo":"MI2", "proprietario_id":"1"}' -H "Content-Type:application/json"
@app.route("/incluir_celular", methods=['POST'])
def incluir_celular():
    dados = request.get_json()

    try:
        # cria o celular
        nova = Celular(**dados)

        # realiza a persistência
        db.session.add(nova)
        db.session.commit()

        return jsonify({"resultado": "ok", "detalhes": "ok"})
    
    except Exception as e:
        return jsonify({"resultado": "erro", "detalhes": str(e)})