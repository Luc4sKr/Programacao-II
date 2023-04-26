from public.config import *

class Pessoa(db.Model):
    # atributos da pessoa
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Text)
    email = db.Column(db.Text)
    telefone = db.Column(db.Text)

    # método para expressar a pessoa em forma de texto
    def __str__(self):
        return f"{self.id}, {self.nome}, {self.email}, {self.telefone}"
    
    # expressao da classe no formato json
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "telefone": self.telefone
        }
