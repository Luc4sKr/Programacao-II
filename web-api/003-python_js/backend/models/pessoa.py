from datetime import datetime

class Pessoa:
    def __init__(self, nome="", email="", telefone="", nascimento=datetime(1, 1, 1)):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.nascimento = nascimento

    def __str__(self):
        return f'{self.nome}, {self.email}, {self.telefone}'

    def json(self):
        return {
            "nome": self.nome,
            "email": self.email,
            "telefone": self.telefone,
            "nascimento": self.nascimento.strftime("%d, %b, %Y")
        }
