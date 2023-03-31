from configs.config import *
from configs.routes_config import *

from models.user import User

@app.route("/users", methods=["GET"])
def select_all_users():
    user_obj = User.query.all()
    user_json = [user.json() for user in user_obj]

    return generate_response(200, "users", user_json)
