import os

from app import app, db
from config import *

with app.app_context():
    if os.path.exists(db_file):
        os.remove(db_file)
         
    db.create_all()