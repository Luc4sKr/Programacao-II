import os

path = os.path.dirname(f"{os.path.abspath(__file__)}")
db_file = os.path.join(f"{path}/app/db", "database.db")


DEBUG = True

SQLALCHEMY_DATABASE_URI = f"sqlite:///{db_file}"
SQLALCHEMY_TRACK_MODIFICATIONS = False