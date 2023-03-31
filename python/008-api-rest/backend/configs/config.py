from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# configurações específicas para o SQLite
path = os.path.dirname(os.path.abspath(__file__))
db_file = os.path.join(path, 'pessoas.db')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + db_file

db = SQLAlchemy(app)