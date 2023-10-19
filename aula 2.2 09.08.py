class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        self.idade += anos
        if self.idade <= 21:
            self.crecer(0.5 * anos)

    def engoradar(self, kgs):
        self.peso += kgs

    def emagrecer(self, kgs):
        self.peso -= kgs

    def crescer(self, cm):
        if cm > 0:
            self.altura += cm
