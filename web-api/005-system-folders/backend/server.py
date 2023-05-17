from config.configs import *

from routes import *

with app.app_context():
    CORS(app)
   
    @app.route("/")
    def index():
        return "backend operante"

    app.run(debug=True) 
