from config.configs import *
from models.pessoa import Pessoa


class Celular(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.Text)
    modelo = db.Column(db.Text)
    proprietario_id = db.Column(db.Integer, db.ForeignKey(Pessoa.id), nullable=False)

    proprietario = db.relationship("Pessoa")
    
    def __str__(self):
        return f"{self.marca}, {self.modelo}, {self.proprietario}"
       

    def json(self):
        return {
            "id":self.id,
            "modelo":self.modelo,
            "marca":self.marca,
            "proprietario":self.proprietario.json()
        }