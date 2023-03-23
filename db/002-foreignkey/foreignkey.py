from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


# CONFIGURAÇÕES ----------------------------------------------------------------
app = Flask(__name__) 
# sqlalchemy usando sqlite

# obter o caminho do arquivo atual
caminho = os.path.dirname(os.path.abspath(__file__))

# concatenar o caminho com o nome do arquivo de banco de dados
arquivobd = os.path.join(caminho, 'pessoas.db')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + arquivobd

# vínculo com o SQLAlchemy
db = SQLAlchemy(app) 
# ------------------------------------------------------------------------------

# CONTEXTO ---------------------------------------------------------------------
with app.app_context():

    class Pessoa(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        nome = db.Column(db.Text)
        email = db.Column(db.Text)

        def __str__(self):
            return f'(id={self.id}) {self.nome}, {self.email}'
        

    class Celular(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        modelo = db.Column(db.Text)
        marca = db.Column(db.Text)

        # atributo de relacionamento de chave estrangeira
        proprietario_id = db.Column(db.Integer, db.ForeignKey(Pessoa.id), nullable=False)

        # atributo de acesso ao objeto
        proprietario = db.relationship("Pessoa")
        
        def __str__(self):
            return f'{self.modelo}, {self.marca}, {self.proprietario}'


    # criar tabelas
    db.create_all()

    # teste da classe Pessoa: duas instâncias
    p1 = Pessoa(nome="João da Silva", email="josilva@gmail.com")
    p2 = Pessoa(nome="Maria Oliveira", email="molive@gmail.com")

    cll1 = Celular(marca="Samsung", modelo="J8", proprietario_id=1)    

    # persistir as duas pessoas
    db.session.add(p1)
    db.session.add(p2)

    db.session.add(cll1)

    db.session.commit()

    print(p1)
    print(cll1.proprietario.nome)
# ------------------------------------------------------------------------------