from configs.config import *
from configs.routes_config import *

from models.user import User

@app.route("/user", methods=["POST"])
def create_user():
    body = request.get_json()

    try:
        user = User(name=body["name"], email=body["email"])
        db.session.add(user)
        db.session.commit()
        
        return generate_response(201, "user", user.json(), "Criado com sucesso")
    
    except Exception as e:
        print('Erro', e)
        
        return generate_response(400, "user", {}, "Erro ao cadastrar")