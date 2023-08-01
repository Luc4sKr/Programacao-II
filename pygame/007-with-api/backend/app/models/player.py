import datetime

from app import db, ma
from .weapon import Weapon


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.datetime.now())

    max_score = db.Column(db.Integer, nullable=False)
    coins = db.Column(db.Integer, nullable=False)

    weapon_id = db.Column(db.Integer, db.ForeignKey(Weapon.id), nullable=False)
    weapon = db.relationship("Weapon")


class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "username", "email", "password", "created_on", "max_score", "coins")


player_schema = UserSchema()
players_schema = UserSchema(many=True)