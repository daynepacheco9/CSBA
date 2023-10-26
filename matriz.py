from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class Matriz:
    def __init__(self):
        self.dados = [[0,0,0],[0,0,0],[0,0,0]]

    def setValor(self, lin, col, valor):
        self.dados[lin][col] = valor

    def setcalcularMaior(self):
        maior = 0
        for i in range(3):
            for j in range(3):
                if self.dados[i][j] > maior:
                    maior = self.dados[i][j]
        return maior 

    def setcalcularMenor(self):
        menor = 0
        for i in range(3):
            for j in range(3):
                if self.dados[i][j] != 0:
                    if self.dados[i][j] > menor:
                        menor = self.dados[i][j]
        return menor
    def setsomaDiagonal(self):
        soma = 0
        for i in range(3):
            for j in range(3):
                if i == j:
                    soma += self.dados[i][j]
        return soma
    
    def setcalcularSoma(self):
        somaP = 0
        for i in range(3):
            for j in range(3):
                soma += self.dados[i][j]
        return somaP
    
    def setcalcularProduto(self):
        produto = 1
        for i in range(3):
            for j in range(3):
                if self.dados[i][j] != 0:
                    produto *= self.dados[i][j]
        return produto

class Tela(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.minha_matriz = Matriz()

    def validar(self, tipoValor):
        try:
            value = int(tipoValor)
        except:
            tipoValor = ''
            value = 0
        return value

    def definir_valor(self, lin, col, campo):
        dado = self.ids[campo].text
        dadoInt = self.validar(dado)

        self.minha_matriz.setValor(lin,col,dadoInt)

    def tipos(self,tipo):
        
        if tipo == 'MAIOR VALOR':
            maior = self.minha_matriz.setcalcularMaior()
            self.ids.valor.text = str(maior)
            
        elif tipo == 'MENOR VALOR':
            menor = self.minha_matriz.setcalcularMaior()
            self.ids.valor.text = str(menor)

        elif tipo == 'SOMA DOS ELEMENTOS':
            soma = self.minha_matriz.setcalcularSoma()
            self.ids.valor.text = str(soma)

        elif tipo == 'SOMA NA DIAGONAL':
            somaP = self.minha_matriz.setcalcularSoma()
            self.ids.valor.text = str(somaP)
        
        elif tipo == 'PRODUTO DOS ELEMENTOS':
            produto = self.minha_matriz.setcalcularProduto()
            self.ids.valor.text = str(produto) 



    def limpar(self):
        self.ids['q2'].text = ''
        self.ids['q2'].text = ''
        self.ids['q3'].text = ''
        self.ids['q4'].text = ''
        self.ids['q5'].text = ''
        self.ids['q6'].text = ''
        self.ids['q7'].text = ''
        self.ids['q8'].text = ''
        self.ids['q9'].text = ''
        self.ids.mensagem.text = ''
        

    def sair(self):
        App.get_running_app().stop()
        Window.close()

class MatrizApp(App):
    def build(self):
        
        return Tela()


MatrizApp().run()
    