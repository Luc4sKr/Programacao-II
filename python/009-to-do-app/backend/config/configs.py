from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

path = os.path.dirname(os.path.abspath(__file__))
file_db = os.path.join(path, "tasks.db")
app.config["SQLALCHEMY_DATABASE_URI"] + "sqlite:///" + file_db

db = SQLAlchemy(app)
