from app import db, ma


class Weapon(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    image_path = db.Column(db.String(120), nullable=False)
    damage = db.Column(db.Integer, nullable=False)

    def __init__(self, iamge_path, damage):
        self.image_path = iamge_path
        self.damage = damage


class WeaponSchema(ma.Schema):
    class Meta:
        filds = ("id", "image_path", "damage")


weapon_schema = WeaponSchema()
weapons_schemas = WeaponSchema(many=True)