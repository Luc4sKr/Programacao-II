from config import *

from models.user import User


with app.app_context():

    if os.path.exists(db_file):
        os.remove(db_file)

    # criar tabelas
    db.create_all()

    print("Banco de dados e tabelas criadas")
