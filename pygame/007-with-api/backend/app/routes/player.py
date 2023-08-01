from app import app
from ..views import player


@app.route("/players", methods=["GET"])
def get_players():
    return player.get_players()

@app.route("/player/<id>", methods=["GET"])
def get_player(id):
    return player.get_player(id)

@app.route("/player", methods=["POST"])
def post_player():
    return player.post_player()
