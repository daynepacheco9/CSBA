from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class Tela(BoxLayout):
    def realiza_soma(self):
        valor_de_num1 = int(self.ids['num1'].text)
        valor_de_num2 = int(self.ids['num2'].text)
        resposta = valor_de_num1 + valor_de_num2
        self.ids.resposta.text = str(resposta)

    def realiza_sub(self):
        valor_de_num1 = int(self.ids['num1'].text)
        valor_de_num2 = int(self.ids['num2'].text)
        resposta = valor_de_num1 - valor_de_num2
        self.ids.resposta.text = str(resposta)

    def realiza_mult(self):
        valor_de_num1 = int(self.ids['num1'].text)
        valor_de_num2 = int(self.ids['num2'].text)
        resposta = valor_de_num1 * valor_de_num2
        self.ids.resposta.text = str(resposta)

    def realiza_div(self):
        valor_de_num1 = int(self.ids['num1'].text)
        valor_de_num2 = int(self.ids['num2'].text)
        resposta = valor_de_num1 / valor_de_num2
        self.ids.resposta.text = str(resposta)

class CalculadoraApp(App):
    def build(self):
        Window.size = (400,400)
        self.title = 'Calculadora Básica'
        return Tela()
    
CalculadoraApp().run()