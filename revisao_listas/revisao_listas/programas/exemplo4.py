# Funcao para inserir um elemento na lista: funcao append

lista_nomes = ["Joao", "Pedro", "Ana", "Antonio"]

# Inserir mais um elemento na lista
nome = input("Digite um nome para inserir na lista: ")
lista_nomes.append(nome)

print(lista_nomes)

# OBS: o append insere um elemento no final da lista

# Funcao para remover um elemento da lista: funcao pop

# 2 formas:
lista_nomes.pop() # remove o ultimo elemento
print(lista_nomes)

lista_nomes.pop(0) # remove o primeiro elemento
print(lista_nomes)

# Criar uma lista com 10 numeros digitados pelo usuario
lista_numeros = [] # criando uma lista vazia

for i in range(10):
    num = int(input("Digite um numero para inserir na lista: "))
    lista_numeros.append(num)

print(lista_numeros)