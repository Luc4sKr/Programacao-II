from public.config import *

from models.pessoa import *
from models.exame import *
from models.exame_realizado import *
from models.respirador import *

# inserindo a aplicação em um contexto :-/
with app.app_context():

    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    # criar tabelas
    db.create_all()

    print("Banco de dados e tabelas criadas")
