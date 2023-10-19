class Dependente:
    def _init_(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Imovel:
    def _init_(self, tipo, endereco, valor):
        self.tipo = tipo
        self.endereco = endereco
        self.valor = valor

class Contribuinte:
    def _init_(self, nome, cpf, rendimentos, dependente, imovel):
        self.nome = nome
        self.__cpf = cpf
        self.rendimentos = rendimentos
        self.dependente = dependente
        self.imovel = imovel

    def calcular_imposto(self):
        imposto_rendimentos = 0.05 * self.rendimentos
        imposto_imovel = 0.03 * self.imovel.valor
        deducao_dependente = 0.1 * self.imovel.valor
        imposto_total = imposto_rendimentos + imposto_imovel - deducao_dependente
        return imposto_total

# Cadastro de um contribuinte com seus respectivos dependentes e imóvel
dependente = Dependente("João", 12)
imovel = Imovel("Casa", "Rua A, 123", 200000)
contribuinte = Contribuinte("Ana", "123.456.789-00", 50000, dependente, imovel)

# Impressão das informações relativas ao contribuinte
print("Nome:", contribuinte.nome)
print("CPF:", contribuinte.Contribuintecpf)  # Acessando o cpf privado usando _Classe_atributo
print("Rendimentos:", contribuinte.rendimentos)
print("Dependente:", contribuinte.dependente.nome, "Idade:", contribuinte.dependente.idade)
print("Imóvel:", contribuinte.imovel.tipo, "Endereço:", contribuinte.imovel.endereco, "Valor:", contribuinte.imovel.valor)

# Cálculo e impressão do imposto devido
imposto_devido = contribuinte.calcular_imposto()
print("Imposto devido:", imposto_devido)