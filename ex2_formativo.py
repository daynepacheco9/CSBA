class Contribuinte:
    def __init__(self, nome, cpf, rendi_anual, dependentes, imoveis):
        self.nome = nome 
        self.__cpf = cpf
        self.rendi_anual = rendi_anual
        self.listaDependentes = []
        self.listaImoveis = []
        for i in dependentes:
            self.listaDependentes.append(i)

        for j in imoveis:
            self.listaImoveis.append(j)

    def mostrarCpf(self):
        return self.__cpf
    
    def imposto(self):
        soma = (self.rendimento_anual * 0.05) + (self.listaImoveis *0.03)
        dep  = soma * 0,1
        rt = soma - dep
        return rt
    
    def mostrarListadepen(self):
        return self.listaDependentes
    
    def add_dependente(self,depen):
        if depen not in self.listaDependentes:
            self.listaDependentes.append(depen)

    def mostrarListaimoveis(self):
        return self.listaImoveis
    
    def add_imoveis(self,imov):
        if imov not in self.listaImoveis:
            self.listaImoveis.append(imov)

class Dependentes:
    def __init__(self, nome , idade):
        self.nome = nome
        self.idade = idade

class Imoveis:
    def __init__(self, tipo, endereco, valor):
        self.tipo = tipo
        self.endereco = endereco
        self.valor = valor

