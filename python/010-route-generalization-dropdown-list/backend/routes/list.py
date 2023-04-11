from public.config import *
from models.pessoa import *
from models.exame import *
from models.exame_realizado import *
from models.respirador import *


@app.route("/listar/<string:classe>")
def listar(classe):
    # obter os dados da classe informada
    dados = None
    
    if classe == "ExameRealizado":
        dados = db.session.query(ExameRealizado).all()
    elif classe == "Pessoa":
        dados = db.session.query(Pessoa).all()
    elif classe == "Respirador":
        dados = db.session.query(Respirador).all()
    elif classe == "Exame":
        dados = db.session.query(Exame).all()
    
    if dados:
      # converter dados para json
      lista_jsons = [x.json() for x in dados]

      meujson = {"resultado": "ok"}
      meujson.update({"detalhes": lista_jsons})
      return jsonify(meujson)
    else:
      return jsonify({"resultado":"erro", "detalhes":"classe informada inválida: "+classe})

    '''
exemplo de teste:
$ curl localhost:5000/listar/Exame
{
  "detalhes": [
    {
      "id": 1,
      "nome": "B12",
      "unidade": "pg/mL",
      "vr": "239 a 931"
    }
  ],
  "resultado": "ok"
}

$ curl localhost:5000/listar/ExameRealizado
{
  "detalhes": [
    {
      "data": "02/02/2020",
      "exame": {
        "id": 1,
        "nome": "B12",
        "unidade": "pg/mL",
        "vr": "239 a 931"
      },
      "exame_id": 1,
      "id": 1,
      "pessoa": {
        "email": "josilva@gmail.com",
        "id": 4,
        "nome": "Jo\u00e3o da Silva",
        "telefone": "47 99012 3232"
      },
      "pessoa_id": 4,
      "resultado": "219,0 pg/mL"
    }
  ],
  "resultado": "ok"
}

'''
