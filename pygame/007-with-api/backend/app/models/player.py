import datetime

from app import db, ma
from .weapon import Weapon


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.datetime.now())

    max_score = db.Column(db.Integer, nullable=True)
    #max_time = db.Column(db.)
    coins = db.Column(db.Integer)

    weapon_id = db.Column(db.Integer, db.ForeignKey(Weapon.id), nullable=False)
    weapon = db.relationship("Weapon")

    def __init__(self, username, email, password, created_on, max_score, max_time, coins):
        self.username = username
        self.email = email
        self.password = password
        self.created_on = created_on
        self.max_score = max_score
        self.max_time = max_time
        self.coins = coins


class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "username", "email", "password", "created_on", "max_score", "max_time", "coins")


user_schema = UserSchema()
users_schema = UserSchema(many=True)