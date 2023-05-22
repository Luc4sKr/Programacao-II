from config import *

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    """
    name
    email
    created_on
    """