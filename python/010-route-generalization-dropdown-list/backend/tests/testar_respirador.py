from public.config import *
from models.pessoa import Pessoa
from models.respirador import Respirador

def run():
  print("==============================================")
  print("TESTE DE RESPIRADOR")

  p1 = Pessoa(nome = "Mário Andrade", email = "maan@gmail.com", 
      telefone = "47 91234 1423")
  db.session.add(p1)
  db.session.commit()

  r1 = Respirador(codigo="001A", data_aquisicao="24/03/2020")
  db.session.add(r1)
  db.session.commit()
  print(r1)

  r2 = Respirador(codigo="002B", data_aquisicao="01/02/2020", pessoa = p1, data_emprestimo="04/02/2020")
  db.session.add(r2)
  db.session.commit()
  print(r2)
  print("==============================================")
