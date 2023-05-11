from config import *
from models import *

# criando contexto para a aplicação :-/
with app.app_context():

    # criar tabelas
    db.create_all()

    print("Tabelas criadas")
