from configs.config import *
from configs.routes_config import *

from models.user import User

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