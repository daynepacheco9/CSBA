class Bola:
    def __init__(self, cor,circ, mat):
        self.cor = cor
        self.circunferencia = circ
        #para deixar privado o atributo tem que colocar dois __
        self.__material = mat

    def trocaCor(self, novaCor):
        self.cor = novaCor

    def mostrarMaterial (self):
        return self.__material
    
    