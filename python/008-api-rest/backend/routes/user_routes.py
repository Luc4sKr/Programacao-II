from configs.config import *
from configs.routes_config import *

from models.user import User


@app.route("/users", methods=["GET"])
def select_all_users():
    user_obj = User.query.all()
    user_json = [user.json() for user in user_obj]

    return generate_response(200, "users", user_json)

@app.route("/user/<id>", methods=["GET"])
def select_user(id):
    user_obj = User.query.filter_by(id=id).first()
    user_json = user_obj.json()

    return generate_response(200, "usuario", user_json)

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
    
@app.route("/user/<id>", methods=["DELETE"])
def deleta_usuario(id):
    user_obj = User.query.filter_by(id=id).first()

    try:
        db.session.delete(user_obj)
        db.session.commit()
        return generate_response(200, "user", user_obj.json(), "Deletado com sucesso")
    
    except Exception as e:
        print('Erro', e)
        return generate_response(400, "user", {}, "Erro ao deletar")