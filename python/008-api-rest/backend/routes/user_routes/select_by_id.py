from configs.config import *
from configs.routes_config import *

from models.user import User

@app.route("/user/<id>", methods=["GET"])
def select_user(id):
    user_obj = User.query.filter_by(id=id).first()
    user_json = user_obj.json()

    return generate_response(200, "usuario", user_json)
