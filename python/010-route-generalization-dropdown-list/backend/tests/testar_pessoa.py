from public.config import *
from models.pessoa import Pessoa

def run():
    print("==============================================")
    print("TESTE DE PESSOA")
    
    p1 = Pessoa(nome = "Teresa Joaquina", email = "tejo@gmail.com", 
    telefone = "47 93022 5231")
    p2 = Pessoa(nome = "Paulo Pedrada", email = "pape@gmail.com", 
        telefone = "47 94321 1234")        
    db.session.add(p1)
    db.session.add(p2)
    db.session.commit()
    print(p1, p2)
    print("==============================================")
