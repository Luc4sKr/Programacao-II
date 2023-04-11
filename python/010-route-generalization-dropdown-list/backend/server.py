from public.config import *

from routes.list import *
from routes.include import *

# rota padrão
@app.route("/")
def inicio():
    return 'backend com rotas generalizadas de listagem'

# inserindo a aplicação em um contexto :-/
with app.app_context():

    app.run(debug=True)
