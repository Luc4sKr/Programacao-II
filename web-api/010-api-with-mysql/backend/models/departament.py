from public.configs import *
from .employee import Employee

class Departament(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(254), nullable=False)
    
    manager_id = db.Column(db.Integer, db.ForeignKey(Employee.id), nullable=False)
    manager = db.relationship("Employee")

    def __str__(self):
        return f"{self.id}, {self.name}, {self.manager}"
    
    def josn(self):
        return {
            "id": self.id,
            "name": self.name
        }