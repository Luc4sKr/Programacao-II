from public.config import *
from models import *

# exemplos de caverna
c1 = cave.Cave(is_good_dragon=False, 
             question="O dragão te encontrou, que pena :-(", 
             response="")

c2 = cave.Cave(is_good_dragon=True,
             question="Você encontrou o dragão da matemática, quando é 1+1? Responda com um número.",
             response = "2")

c3 = cave.Cave(is_good_dragon=True,
             question="Você encontrou o dragão de biologia, o conjunto de características que recebemos de nossos pais se chama: 1) fenótipo, ou 2) genótipo?",
             response = "2")

db.session.add(c1)
db.session.add(c2)
db.session.add(c3)
db.session.commit()

# cria alguns exemplos de jogada
j1 = play.Play(player_name="Hylson")
j1.caves.append(c1)
j1.caves.append(c2)

db.session.add(j1)
db.session.commit()

print(c1, c2, c3)
print(j1)
print("Dados inseridos")
