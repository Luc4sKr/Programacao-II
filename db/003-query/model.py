from config import *

class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    email = db.Column(db.String(254))
    telefone = db.Column(db.String(254))

    def __str__(self):
        return f"(id={self.id}) {self.nome}, {self.email}, {self.telefone}"

if __name__ == "__main__":

    # apagar o arquivo, se houver
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    # criar tabelas
    db.create_all()

    # teste da classe Pessoa
    p1 = Pessoa(nome = "João da Silva",  email = "josilva@gmail.com",   telefone = "47 99012 3232")
    p2 = Pessoa(nome = "Maria Oliveira", email = "molive@gmail.com",    telefone = "47 98822 2531")
    p3 = Pessoa(nome = "Joana Tristão",  email = "jotristao@gmail.com", telefone = "47 99123 1289")
    
    # persistir
    db.session.add(p1)
    db.session.add(p2)
    db.session.add(p3)
    db.session.commit()
    
    # localizar uma pessoa por email
    print("Quem tem email molive@gmail.com?")
    alguem = Pessoa.query.filter_by(email='molive@gmail.com').first()
    print(alguem)

    print("Quem tem a expressão 'ri' no nome?")
    pessoas = Pessoa.query.filter(Pessoa.nome.contains('ri'))
    for pessoa in pessoas:
        print(pessoa)

    # localizar uma pessoa pelo ID
    primeira = db.session.get(Pessoa, 1)
    print("Primeira pessoa: " + str(primeira))

    # primeira = Pessoa.query.get(1) -> esta dando warning:
    # method is considered legacy as of the 1.x series of SQLAlchemy

    # atualizar os dados de uma pessoa já carregada na memória (em objeto)
    primeira.email = "josilva@hotmail.com" # original = gmail
    db.session.commit()
    print(primeira)

