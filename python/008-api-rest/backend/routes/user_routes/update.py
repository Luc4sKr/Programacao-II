from configs.config import *
from configs.routes_config import *

from models.user import User

@app.route("/user/<id>", methods=["PUT"])
def atualiza_usuario(id):
    user_obj = User.query.filter_by(id=id).first()
    body = request.get_json()

    try:
        if('name' in body):
            user_obj.name = body['name']
        if('email' in body):
            user_obj.email = body['email']
        
        db.session.add(user_obj)
        db.session.commit()
        return generate_response(200, "user", user_obj.json(), "Atualizado com sucesso")
    
    except Exception as e:
        print('Erro', e)
        return generate_response(400, "user", {}, "Erro ao atualizar")