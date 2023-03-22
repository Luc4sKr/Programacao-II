from config.configs import *
from routes import *

@app.route("/")
def ola():
    return "backend operante"


with app.app_context():

    # criar o banco de dados, caso não esteja criado
    db.create_all()

    # provendo o CORS ao sistema
    CORS(app)

    # iniciar o servidor
    app.run(debug=True)
