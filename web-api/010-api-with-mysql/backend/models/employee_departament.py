from public.configs import *

from .departament import Departament
from .employee import Employee

class Employee_Departament(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)

    departament_id = db.Column(db.Integer, db.ForeignKey(Departament.id), nullable=False)
    departament = db.relationship("Departament")

    manager_id = db.Column(db.Integer, db.ForeignKey(Employee.id), nullable=False)
    manager = db.relationship("Employee")