from config import *
from models.user import User


@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Hello world"})

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    print(data)

    try:
        user = User(**data)
        db.session.add(user)
        db.session.commit()
        
        return jsonify({"message": "successfully registered", "data": data}), 201
    except Exception as e:
        return jsonify({"message": f"unable to create. error: {e}", "data": {}}), 500


if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)
    