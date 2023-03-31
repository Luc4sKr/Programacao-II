from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import update
import os

app = Flask(__name__)

# caminho do arquivo de banco de dados
path = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(path, 'pessoas.db')

# sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # remover warnings
db = SQLAlchemy(app) # vínculo com o SQLAlchemy

# para exibir versões das bibliotecas:
# pip3 freeze
# para instalar requisitos:
# pip3 install -r requirements.txt

app.app_context().push()
