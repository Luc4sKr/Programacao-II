from config.configs import *
from routes import *

@app.route("/")
def index():
    return "backend operante"

with app.app_context():
    db.create_all()
    CORS(app)
    app.run(debug=True)
    