from public.configs import *
from models.departament import Departament

with app.app_context():

    db.create_all()

    print("Tabelas criadas")
