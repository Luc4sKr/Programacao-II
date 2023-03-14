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
        telefone = db.Column(db.Text)

        def __str__(self):
            return f'(id={self.id}) {self.nome}, '+\
                f'{self.email}, {self.telefone}'

    # criar tabelas
    # se alterar a classe, precisa apagar o arquivo para
    # que as tabelas sejam criadas novamente!
    db.create_all()

    # teste da classe Pessoa: duas instâncias
    p1 = Pessoa(nome = "João da Silva", email = "josilva@gmail.com", 
        telefone = "47 99012 3232")
    p2 = Pessoa(nome = "Maria Oliveira", email = "molive@gmail.com", 
        telefone = "47 98822 2531")        

    # persistir as duas pessoas
    db.session.add(p1)
    db.session.add(p2)
    db.session.commit()

    # exibir uma pessoa
    print(p2)
# ------------------------------------------------------------------------------