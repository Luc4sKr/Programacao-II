from config.configs import *


class Pessoa(db.Model):
    # atributos da pessoa
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Text)
    email = db.Column(db.Text)

    # expressar a classe em formato texto
    def __str__(self):
        return f"{self.nome}, {self.email}"

    # expressar a classe em formato json
    def json(self):
        return {
            "nome": self.nome,
            "email": self.email
        }
    