from public.configs import *

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(254), nullable=False)
    email = db.Column(db.String(254), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)

    def __str__(self):
        return f"{self.id}, {self.name}, {self.email}, {self.cpf}"
    
    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "cpf": self.cpf
        }