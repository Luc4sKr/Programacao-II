from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)

path = os.path.dirname(os.path.abspath(__file__))
db_file = os.path.join(path, 'dragons.db')

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + db_file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.app_context().push()
