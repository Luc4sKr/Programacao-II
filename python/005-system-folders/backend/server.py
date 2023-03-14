from config.configs import *
from models.person import Person

from routes import *

with app.app_context():
    CORS(app) # provendo o CORS ao sistema
   
    @app.route("/") # rota padrão
    def ola():
        return "backend operante"

    app.run(debug=True) 
