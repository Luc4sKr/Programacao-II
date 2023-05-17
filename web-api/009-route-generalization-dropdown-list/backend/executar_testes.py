from public.config import *
from tests import *

# inserindo a aplicação em um contexto :-/
with app.app_context():

    testar_pessoa.run()
    testar_respirador.run()
    testar_exame_realizado.run()
