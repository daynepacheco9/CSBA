class Contribuinte:
    def __init__(self, nome, cpf, rend_a, dependente, imovel):
        self.nome = nome
        self.__cpf = cpf
        self.rendimento_anual = rend_a
        self.dependente = dependente
        self.imovel = imovel

    def mostrarCpf(self):
        return self.__cpf
    
    def imposto(self):
        soma = (self.rendimento_anual * 0.05) + (self.imovel *0.03)
        dep  = soma * 0,1
        rt = soma - dep
        return rt

class dependente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class imovel:
    def __init__(self, tipo, endereco, valor):
        self.tipo = tipo
        self.endereco = endereco
        self.valor = valor

