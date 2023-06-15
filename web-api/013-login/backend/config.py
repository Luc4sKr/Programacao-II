import os

DEBUG = True


SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.db')}"
SQLALCHEMY_TRACK_MODIFICATIONS = False