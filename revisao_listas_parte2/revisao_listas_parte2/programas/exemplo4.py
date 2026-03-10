# Criar uma lista com 10 numeros digitados pelo usuario
lista_numeros = [] # criando uma lista vazia

for i in range(10):
    num = int(input("Digite um numero para inserir na lista: "))
    lista_numeros.append(num)

print(lista_numeros)

