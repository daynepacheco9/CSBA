from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class Tela(BoxLayout):

    def tipos(self,tipo):
        
        type1 = self.ids['q1'].text
        try:
            value1 = int(type1)                
        except:
            self.ids['q1'].text = ''
            value1 = 0

        type2 = self.ids['q2'].text
        try:
            value2 = int(type2)                
        except:
            self.ids['q2'].text = ''
            value2 = 0

        type3 = self.ids['q3'].text
        try:
            value3 = int(type3)                
        except:
            self.ids['q3'].text = ''
            value3 = 0

        type4 = self.ids['q4'].text
        try:
            value4 = int(type4)                
        except:
            self.ids['q4'].text = ''
            value4 = 0

        type5 = self.ids['q5'].text
        try:
            value5 = int(type5)                
        except:
            self.ids['q5'].text = ''
            value5 = 0

        type6 = self.ids['q6'].text
        try:
            value6 = int(type6)                
        except:
            self.ids['q6'].text = ''
            value6 = 0

        type7 = self.ids['q7'].text
        try:
            value7 = int(type7)                
        except:
            self.ids['q7'].text = ''
            value7 = 0

        type8 = self.ids['q8'].text
        try:
            value8 = int(type8)                
        except:
            self.ids['q8'].text = ''
            value8 = 0

        type9 = self.ids['q9'].text
        try:
            value9 = int(type9)                
        except:
            self.ids['q9'].text = ''
            value9 = 0
        
        lista = [value1, value2, value3, value4, value5, value6,value7,value8,value9]

        if tipo == 'MAIOR VALOR':
            maior = lista[0]
            for i in range(len(lista)):
                if lista[i] > maior:
                    maior = lista[i]
            self.ids.valor.text = str(maior)
            
        elif tipo == 'MENOR VALOR':
            menor = lista[0]
            for i in range(len(lista)):
                if lista[i] < menor:
                    menor = lista[i]
            self.ids.valor.text = str(menor)


        elif tipo == 'SOMA DOS ELEMENTOS':
            soma_total = 0
            for i in range(len(lista)):
                soma_total += lista[i]
            self.ids.valor.text = str(soma_total)

        elif tipo == 'SOMA NA DIAGONAL':
            self.ids.nome.text = 'O valor da compra de' + self.ids['tx2'].text
            self.ids.mensagem.text = 'Escolhi CRÉDITO 2X' 
        
        elif tipo == 'PRODUTO DOS ELEMENTOS':
            produto = 1
            for i in range(len(lista)):
                if lista[i] != 0:
                    produto *= lista[i]
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
        

    def sair(self):
        App.get_running_app().stop()
        Window.close()

class Matriz(App):
    def build(self):
        
        return Tela()


Matriz().run()
    