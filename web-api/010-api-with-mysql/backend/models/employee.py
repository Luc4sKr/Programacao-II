from public.configs import *
from .person import Person

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    salary = db.Column(db.Float)
    position = db.Column(db.String(254))

    person_id = db.Column(db.Integer, db.ForeignKey(Person.id), nullable=False)
    person = db.relationship("Person")

    

    
    def __str__(self):
        return f"{self.id}, {self.salary}, {self.position}, {self.person}"
    
    def json(self):
        return {
            "id": self.id,
            "salary": self.salary,
            "position": self.position,
            "person": self.person.json(),
            "departament": self.departament.json()
        }