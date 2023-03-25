from config.configs import *
from models.celular import Celular

@app.route("/listar_celulares")
def listar_celulares():
    try:
        # obter os celulares
        lista = db.session.query(Celular).all()

        # converter pra json
        lista_retorno = [x.json() for x in lista]

        # preparar uma parte da resposta: resultado ok
        meujson = {"resultado": "ok"}
        meujson.update({"detalhes": lista_retorno})

        # retornar a lista em json, com resultado ok
        resposta = jsonify(meujson)
        return resposta
    
    except Exception as e:
        return jsonify({"resultado": "erro", "detalhes": str(e)})    