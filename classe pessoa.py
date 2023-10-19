class Pessoa:
    def __init__(self, cor_c, cor_o, nome):
        self.__cor_cabelo = cor_c
        self__cor_olhos = cor_o
        self.__nome = nome

    def mostraNome(self):
        return self.__nome
        
    def mudaCabelo(self, novaCor):
        self.cor_cabelo = novaCor

    def mostraOlhos(self):
        return self.__cor_olhos
    
    def mostrarCabelo(self):
        return self.__cor_cabelo
    
a = Pessoa('loira','Verde','Dayne')

print()