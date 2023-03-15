from config.configs import *

@app.route("/list_person")
def list_person():
    try:
        # obter as pessoas em formato json
        lista_retorno = [x.json() for x in person_list]
        
        myjson = {"resultado": "ok"}
        myjson.update({"detalhes": lista_retorno})

        # retornar a lista de pessoas json, com resultado ok
        resp = jsonify(myjson)
    except Exception as e:
        resp = jsonify({"result": "error", "details": str(e)})

    return resp