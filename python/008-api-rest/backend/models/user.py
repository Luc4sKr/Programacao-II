from configs.config import *

class User(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100))

    def __str__(self):
        return f"{self.id}, {self.name}, {self.email}"

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email 
        }