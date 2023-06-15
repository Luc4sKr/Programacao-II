from app import app, db
from app.models.users import Users


if __name__ == "__main__":
    with app.app_context():

        user1 = Users("lucas", "123123", "Lucas", "lucas@gmail.com")
        db.session.add(user1)
        db.session.commit()
