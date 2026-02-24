# Criando as 3 listas vazias
lista_numeros = []
lista_pares = []
lista_impares = []

# Solicitar 10 números inteiros e adiciona-los na lista_numeros
for i in range(10): # cont vai variar de 0 a 9
    num = int(input("Digite um número para inserir na lista"))
    lista_numeros.append(num)

# Percorrer a lista_numeros para inserir os pares na lista_pares e impares na lista_impares
for i in range(10):
    if (lista_pares [i] % 2 == 0):
        print()