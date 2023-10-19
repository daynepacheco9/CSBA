from ex_formativo import*

i = imovel('sobrado','odir susin',300000)
d = dependente('day', 20)
c = Contribuinte('dmas','12312312323',20000,d,i)

print('Nome:', c.nome)
print('CPF:', c.mostrarCpf())
print('Rendimento Anual:', c.rendimento_anual)
print(f'Dependente {c.dependente.nome} com idade {c.dependente.idade}.')
print('Imóvel do tipo:', c.imovel.tipo)
print('Endereço:',c.imovel.endereco)
print('Valor:',c.imovel.valor)
print('Imposto devido:', c.imposto())