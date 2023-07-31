from flask import request, jsonify
from app import db, create_access_token
from ..models.player import Player, player_schema, players_schema
from werkzeug.security import generate_password_hash, check_password_hash


def post_player():
    data = request.json()
    data["password"] = generate_password_hash(data["password"])

    try:
        player = Player(**data)
        db.session.add(player)
        db.session.commit()
        result = player_schema.dump(player)

        return jsonify({"message": "successfully registered", "data": result}), 201

    except:
        return jsonify({"message": "unable to create", "data": {}}), 500

