from app import app
from ..views import users
from flask import jsonify



@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Hello World!"})


@app.route("/users", methods=["POST"])
def post_user():
    return users.post_user()