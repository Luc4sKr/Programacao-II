from public.config import *


class Cave(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text)
    response = db.Column(db.Text)
    is_good_dragon = db.Column(db.Boolean)

    def __str__(self):
        return f"id - {self.id}, {self.question}, {self.response}, {self.is_good_dragon}"
