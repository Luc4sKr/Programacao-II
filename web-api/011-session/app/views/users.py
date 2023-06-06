from app import db
from flask import request, jsonify
from ..models.users import Users, user_schema, users_schema
from werkzeug.security import generate_password_hash

def post_user():
    data = request.get_json()

    try:
        data["password"] = generate_password_hash(data["password"])
        
        user = Users(**data)
        db.session.add(user)
        db.session.commit()
        result = user_schema.dump(user)

        return jsonify({"message": "successfully registered", "data": result}), 201

    except:
        return jsonify({"message": "unable to create", "data": {}}), 500
