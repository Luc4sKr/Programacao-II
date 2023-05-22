from flask import Flask, jsonify, request
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
import os
from werkzeug.security import generate_password_hash
import pickle

from flask_cors import CORS

app = Flask(__name__)

"""app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"""

Session(app)

CORS(app) 

# caminho do arquivo de banco de dados - sqlite
path = os.path.dirname(os.path.abspath(__file__)) 
db_file = os.path.join(path, 'database.db')

# sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + db_file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)