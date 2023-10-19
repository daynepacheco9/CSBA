def maior(l):
    ma=l[0] #declarando que o primeiro numero é o maior por enquanto
    n=len(l) #Declarando o tamnho da lista
    for k in range(1,n): #para k variar do segundo numero até o tamanho da lista(que seria o ultimo numero)
        if (l[k]>ma): #SE k for maior que o primeiro numero 
            ma=l[k] #ele troca o primeiro numero pelo maior
    return ma #retorna para o numero maior
def menor(l):
    me=l[0] 
    n=len(l)
    for k in range(1,n):
        if (l[k]<me):
            me=l[k]
    return me
lista=[] #cria uma lista vazia
while(True):
    n=int(input('Digite um numero: ')) #pedir para digitar os numeros
    if(n==0): break #SE n for igual a ele PARA/QUEBRA
    lista.append(n) #ADD os valores de n na lista 
print("Lista lida..:",lista) #mostrar a lista sem 0
print("Menor valor.:",menor(lista))#mostrar o numero maior
print("Maior valor.:",maior(lista))#mostrar o numero menor