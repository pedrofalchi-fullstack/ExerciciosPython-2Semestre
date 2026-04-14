'''
Solicitar que o usuario informe 5 numeros para criar uma lista.
Em seguida, crie uma nova lista com os numeros pares da primeira
lista elevados ao quadrado.
'''

lista_numeros = []
lista_pares = []

# Solicitar 5 numeros para inserir na lista
for i in range(5):
    num = int(input("Digite um numero para inserir na lista: "))
    lista_numeros.append(num)

for i in range(5):
    if (lista_numeros[i] % 2 == 0):
        quadrado = lista_numeros[i] ** 2
        lista_pares.append(quadrado)

print(lista_pares)