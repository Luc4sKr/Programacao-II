from config.configs import *

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.text)
    date = db.Column(db.DateTime)

    def __str__(self):
        return f"{self.id}, {self.task}, {self.date}"
    
    def json(self):
        return {
            "task": self.task,
            "date": self.date
        }
    