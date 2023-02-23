class Pessoa:
    def __init__(self, id, nome, idade) -> None:
        self.id = id
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"{self.id}, {self.nome}, {self.idade}"
    
    def json(self):
        return {
            "id":self.id,
            "nome":self.nome
        }