class Person:
    def __init__(self, name="", email="", phone=""):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"{self.name}, {self.email}, {self.phone}"

    def json(self):
        return {
            "nome" : self.nome,
            "email" : self.email,
            "telefone" : self.telefone 
        }
