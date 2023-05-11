# importações
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# flask
app = Flask(__name__)

# VOCÊ DEVERÁ:
# a) alterar os prefixos dos nomes das tabelas em models.py - coloque o seu nome
# b) CRIAR AS TABELAS
# c) RODAR OS TESTES COM O MYSQL
# DEPOIS, COMENTE A OPÇÃO 2 E DESCOMENTE A OPÇÃO 1
# E FAÇA OS PROCEDIMENTOS A) E B) USANDO O SQLITE

# OPÇÃO 1: sqlalchemy com sqlite -----------------
#path = os.path.dirname(os.path.abspath(__file__)) 
#arquivobd = os.path.join(path, 'pessoa_exame_respirador.db')
#app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd

# OPÇÃO 2: sqlalchemy com mysql ------------------
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://hylsonco_poo2:liberado!#!@62.77.153.140/hylsonco_poo2_2023_1"
#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:testando@191.52.7.111/hylson_poo2"

# configurações comuns para opção 1 e 2
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
