# Atributos: nome, idadem peso, altura.
class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self. peso = peso
        self.altura = altura
    # Métodos: envelhecer, engordar, emagrecer, crescer.
    def envelhecer(self):
        self.idade += 1
        if self.idade > 21:
            self.crescer(0.5)

    def engordar(self, peso_adicional):
        self.peso += peso_adicional

    def emagrecer(self, peso_a_perder):
        self.peso -= peso_a_perder

    def crescer(self, altura_adicional):
        self.altura += altura_adicional