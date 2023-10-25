from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class Tela(BoxLayout):

    def tipos(self,tipo):

        tipo1 = self.ids['q1'].text
        if tipo1 >= '0':
            tipo1 = int(self.ids['q1'].text)
            valor1 = tipo1 * 14.9
        elif tipo1 == '': 
            valor1 = 0

        tipo2 = self.ids['q2'].text
        if tipo2 >= '0':
            tipo2 = int(self.ids['q2'].text)
            valor2 = tipo2 * 10.9
        elif tipo2 == '': 
            valor2 = 0

        tipo3 = self.ids['q3'].text
        if tipo3 >= '0':
            tipo3 = int(self.ids['q3'].text)
            valor3 = tipo3 * 20.9
        elif tipo3 == '': 
            valor3 = 0
        
        tipo4 = self.ids['q4'].text
        if tipo4 >= '0':
            tipo4 = int(self.ids['q4'].text)
            valor4 = tipo4 * 7.9
        elif tipo4 == '': 
            valor4 = 0
        
        tipo5 = self.ids['q5'].text
        if tipo5 >= '0':
            tipo5 = int(self.ids['q5'].text)
            valor5 = tipo5 * 5.9
        elif tipo5 == '': 
            valor5 = 0
        
        tipo6 = self.ids['q6'].text
        if tipo6 >= '0':
            tipo6 = int(self.ids['q6'].text)
            valor6 = tipo6 * 8.9
        elif tipo6 == '': 
            valor6 = 0
        

        valorTotal = valor1 + valor2 + valor3 + valor4 + valor5 + valor6

        if tipo == 'ESPÉCIE':
            self.ids.nome.text = 'O valor da compra de' + self.ids['tx1'].text
            self.ids.mensagem.text = 'Escolhi ESPÉCIE'
            valorPag = valorTotal - (valorTotal * 0.08)
            self.ids.valor.text = 'R$ '+str(valorPag )

        elif tipo == 'PIX':
            self.ids.nome.text = 'O valor da compra de' + self.ids['tx1'].text
            self.ids.mensagem.text = 'Escolhi PIX'
            valorPag = valorTotal - (valorTotal * 0.05)
            self.ids.valor.text = 'R$ '+str(valorPag)

        elif tipo == 'CRÉDITO':
            self.ids.nome.text = 'O valor da compra de' + self.ids['tx1'].text
            self.ids.mensagem.text = 'Escolhi CRÉDITO'
            valorPag = valorTotal 
            self.ids.valor.text = 'R$ '+str(valorPag)

        elif tipo == 'CRÉDITO 2X':
            self.ids.nome.text = 'O valor da compra de' + self.ids['tx1'].text
            self.ids.mensagem.text = 'Escolhi CRÉDITO 2X' 
            valorPag = (valorTotal + (valorTotal * 0.05))/2
            self.ids.valor.text = 'R$ '+str(valorPag) + ' em 2X'


    def limpar(self):
        self.ids['q1'].text = ''
        self.ids['q2'].text = ''
        self.ids['q3'].text = ''
        self.ids['q4'].text = ''
        self.ids['q5'].text = ''
        self.ids['q6'].text = ''
        self.ids['tx1'].text = ''
        self.ids['valor'].text = ''
        self.ids['mensagem'].text = ''
        self.ids['nome'].text = ''
        self.ids.ck1.active = False
        

    def sair(self):
        App.get_running_app().stop()
        Window.close()

class CodigoMequikApp(App):
    def build(self):
        
        return Tela()


CodigoMequikApp().run()
    




