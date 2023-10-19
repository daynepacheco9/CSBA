class Quadrado:
    def __inif__(self, lado):
        self.lado = lado

    def mudaLado(self, novoLado):
        self.lado = novoLado

    def mostraLado(self):
        return self.lado
        
    def calculaArea(self):
        return self.lado**2
    
#crie dois quadrados um com lado 10 outro com lado 15
q1 = Quadrado(10)
q2 = Quadrado(15)

#mostrar a area dos dois quadrados
print("A area de q1= ",q1.calculaArea())
print("A area de q2= ",q2.calculaArea())

#duplique o lado do primeiro quadrado
q1.mudaLado(2*q1.mostraLado())

#mostra a nova area dele
print('a nova area do q1 é', q1.calculeArea())

