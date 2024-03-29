import datetime

from app import db, ma, fields
from .weapon import Weapon, WeaponSchema


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.datetime.now())

    max_score = db.Column(db.Integer, nullable=False)
    coins = db.Column(db.Integer, nullable=False)

    weapon_id = db.Column(db.Integer, db.ForeignKey(Weapon.id), nullable=False)
    weapon = db.relationship("Weapon", backref="weapon")


class PlayerSchema(ma.Schema):
    class Meta:
        model = Player
        #fields = ("id", "username", "email", "password", "created_on", "max_score", "coins", "weapon_id")
    
    username = fields.Str()
    weapon = fields.Nested(WeaponSchema())

player_schema = PlayerSchema()
players_schema = PlayerSchema(many=True)