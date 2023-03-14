from config.configs import *
from models.person import Person

@app.route("/include_person", methods=['POST'])
def incluir():
    data = request.get_json()
    print(data)

    try:
        # cria a pessoa 
        new_person = Person(**data)

        # realiza a persistência da nova pessoa
        person_list.append(new_person)

        # tudo certo, resposta de sucesso
        return jsonify({"resultado": "ok", "detalhes":"ok"})
    
    except Exception as e:
        # informar mensagem de erro
        return jsonify({"resultado": "erro", "detalhes":str(e)})
