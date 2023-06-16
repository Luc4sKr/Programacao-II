from app import *
from flask import request, jsonify
from werkzeug.security import check_password_hash

from .users import user_by_username

def auth():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return jsonify({'message': 'could not verify', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401
    
    user = user_by_username(auth.username)
    if not user:
        return jsonify({'message': 'user not found', 'data': []}), 401

    if user and check_password_hash(user.password, auth.password):
        token = create_access_token(identity=user.username)
        
        return jsonify({'message': 'Validated successfully', 'token': token})

    return jsonify({'message': 'could not verify', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401