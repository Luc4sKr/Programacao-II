from app import app
from ..views import player

@app.route("/player", methods=["POST"])
def post_player():
    return player.post_player()