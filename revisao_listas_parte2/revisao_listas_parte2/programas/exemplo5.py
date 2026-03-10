'''
Dadas 2 listas com 10 numeros inteiros, crie uma terceira lista
com as somas dos elementos correspondentes das 2 primeiras
listas.
'''

# criacao das 3 listas vazias
listaA = []
listaB = []
listaC = []

# Solicitar que o usuario informe os 10 numeros da primeira lista
for i in range(10):
    num = int(input("Digite um numero para inserir na lista A: "))
    listaA.append(num)

# Solicitar que o usuario informe os 10 numeros da segunda lista
for i in range(10):
    num = int(input("Digite um numero para inserir na lista B: "))
    listaB.append(num)

# Somar os numeros correspondentes da listaA e da listaB e adicionar na listaC
for i in range(10):
    soma = listaA[i] + listaB[i]
    listaC.append(soma)

print(listaC)



