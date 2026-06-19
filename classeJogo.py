class heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
        self.armas = {
            "mago": "Magia",
            "guerreiro": "Espada",
            "monge": "Artes Marciais",
            "ninja": "Shuriken"
        }
    
    def ataque(self):
        if self.tipo in self.armas:
            return f"O {self.nome} de Classe {self.tipo} atacou usando {self.armas[self.tipo]}"
heroi1 = heroi("Gandalf", 2019, "mago");
heroi2 = heroi("Conan", 35, "guerreiro");
print(heroi1.ataque());
print(heroi2.ataque());
        

        