from public.config import *
from models.pessoa import *
from models.exame import *
from models.exame_realizado import *
from models.respirador import *


@app.route("/incluir/<string:classe>", methods=['post'])
def incluir(classe):
    # receber as informações do novo objeto
    dados = request.get_json()  

    try:  
        nova = None
        if classe == "ExameRealizado":
            nova = ExameRealizado(**dados)
        elif classe == "Pessoa":
            nova = Pessoa(**dados)
        elif classe == "Respirador":
            nova = Respirador(**dados)
        elif classe == "Exame":
            nova = Exame(**dados)

        db.session.add(nova)   # adicionar no BD
        db.session.commit()    # efetivar a operação de gravação

        # retorno de sucesso :-)
        return jsonify({"resultado": "ok", "detalhes": "ok"})
    
    except Exception as e:  # em caso de erro...
        # informar mensagem de erro :-(
        return jsonify({"resultado": "erro", "detalhes": str(e)})
