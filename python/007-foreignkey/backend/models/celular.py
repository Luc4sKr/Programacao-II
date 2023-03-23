from config.configs import *

from models.pessoa import Pessoa

class Celular(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.Text)
    marca = db.Column(db.Text)

    # atributo de relacionamento de chave estrangeira
    proprietario_id = db.Column(db.Integer, db.ForeignKey(Pessoa.id), nullable=False)

    # atributo de acesso ao objeto
    proprietario = db.relationship("Pessoa")
    
    def __str__(self):
        return f'''
        {self.modelo}, {self.marca}, {self.proprietario}
        '''

    def json(self):
        return {
            "id":self.id,
            "modelo":self.modelo,
            "marca":self.marca,
            "proprietario":self.proprietario.json()
        }

