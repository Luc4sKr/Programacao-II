from app import db, create_access_token
from flask import request, jsonify
from ..models.users import Users, user_schema, users_schema
from werkzeug.security import generate_password_hash, check_password_hash

def post_user():
    data = request.get_json()
    data["password"] = generate_password_hash(data["password"])

    try:     
        user = Users(**data)
        db.session.add(user)
        db.session.commit()
        result = user_schema.dump(user)

        return jsonify({"message": "successfully registered", "data": result}), 201

    except:
        return jsonify({"message": "unable to create", "data": {}}), 500

def update_user(id):
    data = request.get_json()

    user = Users.query.get(id)

    if not user:
        return jsonify({"message": "user don't exist", "data": {}}), 404
    
    pass_hash = generate_password_hash(data["password"])
    
    try:
        user.username = data["username"]
        user.password = pass_hash
        user.name = data["name"]
        user.email = data["email"]

        db.session.commit()

        result = user_schema.dump(user)
        return jsonify({"message": "successfully updated", "data": result})
    except:
        return jsonify({"message": "unable to update", "data": {}}), 500
    
def get_users():
    users = Users.query.all()

    if users:
        result = users_schema.dump(users)
        return jsonify({"message": "successfully fetched", "data": result})
    
    return jsonify({"message": "nothing found", "data": {}})

def get_user(id):
    user = Users.query.get(id)

    if user:
        result = user_schema.dump(user)
        return jsonify({"message": "sucessfully fetched", "data": result}), 201

    return jsonify({"message": "user don't exist", "data": {}}), 404

def delete_user(id):
    user = Users.query.get(id)

    if not user:
        return jsonify({"message": "user don't exist", "data": {}}), 404
    
    try:
        db.session.delete(user)
        db.session.commit()

        result = user_schema.dump(user)

        return jsonify({"message": "seccessfully deleted", "data": result}), 200
    except:
        return jsonify({"message": "unable to create", "data": {}}), 500

def user_by_username(username):
    try:
        return Users.query.filter(Users.username == username).one()
    except:
        return None