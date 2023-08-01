from flask import request, jsonify
from app import db, create_access_token
from ..models.player import Player, player_schema, players_schema
from werkzeug.security import generate_password_hash, check_password_hash


def get_players():
    players = Player.query.all()

    if players:
        result = players_schema.dump(players)
        return jsonify({"message": "successfully fetched", "data": result})
    return jsonify({"message": "nothing found", "data": {}})

def get_player(id):
    player = Player.query.get(id)

    if player:
        result = player_schema.dump(player)
        return jsonify({"message": "sucessfully fetched", "data": result}), 201

def post_player():
    data = request.get_json()
    data["password"] = generate_password_hash(data["password"])

    print(data)

    try:
        player = Player(**data)
        db.session.add(player)
        db.session.commit()
        result = player_schema.dump(player)

        return jsonify({"message": "successfully registered", "data": result}), 201

    except:
        return jsonify({"message": "unable to create", "data": {}}), 500

