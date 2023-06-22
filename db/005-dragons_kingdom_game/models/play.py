from public.config import *
from .cave import Cave

class Play(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(50))

    caves = db.relationship("Cave", secondary="cave_of_move")
    
    def __str__(self):
        s = f'''
        Jogador: {self.player_name}
        '''
        for c in self.caves:
            s += f'\n passou em: {c}'
        return s


cave_of_move = db.Table('cave_of_move', db.metadata,
    db.Column('id_cave', db.Integer, db.ForeignKey(Cave.id)),
    db.Column('id_play', db.Integer, db.ForeignKey(Play.id))
)
