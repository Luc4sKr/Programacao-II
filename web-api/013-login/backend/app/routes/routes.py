from flask import jsonify

from app import app
from ..views import users

@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Hello World"})