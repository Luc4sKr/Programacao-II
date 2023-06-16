from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = Flask(__name__)
CORS(app)
app.config.from_object("config")

db = SQLAlchemy(app)
jwt = JWTManager(app)
ma = Marshmallow(app)

from .models import *
from .views import users
from .routes import routes