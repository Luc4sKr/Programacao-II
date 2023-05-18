from public.configs import *
from models.departament import Departament
from models.employee import Employee
from models.employee_departament import Employee_Departament


with app.app_context():

    db.create_all()

    print("Tabelas criadas")
