from app import db, ma


class Weapon(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    image_path = db.Column(db.String(120), unique=True, nullable=False)
    damage = db.Column(db.Integer, nullable=False)


class WeaponSchema(ma.Schema):
    class Meta:
        model = Weapon
        filds = ("id", "image_path", "damage")


weapon_schema = WeaponSchema()
weapons_schemas = WeaponSchema(many=True)