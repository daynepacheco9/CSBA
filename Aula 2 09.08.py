class Bola:
    def __init__(self,cor,circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self,novaCor):
        self.cor = novaCor

    def mostraCor(self):
        return self.cor
    
#prova ele da o diagrama, pede para criar a classe e saber manipular ela


#criar bola de plastico azul pequena 
bola_azul = Bola("Azul", 10 ,"PLastico") 

#mostrar cor da bola
print('A cor da bola é ', bola_azul.mostraCor())

bola_azul.trocaCor("amarelo")
print("a nova cora da bola é",bola_azul.mostraCor())

#enxer mais a bola
bola_azul.circunferencia = 15
