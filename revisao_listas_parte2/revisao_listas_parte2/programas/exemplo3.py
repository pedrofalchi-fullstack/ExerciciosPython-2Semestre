# Funcoes utilizadas em listas

lista_precos = [25.70, 30.70, 140.20, 250.70]

# 1) Tamanho da lista: funcao len
tamanho = len(lista_precos)
print(f"O tamanho da lista eh {tamanho}")

# 2) Somatorio dos elementos da lista: funcao sum
soma = sum(lista_precos)
print(f"O somatorio dos precos eh {soma:.2f}")

# 3) Maior elemento da lista: funcao max
maior = max(lista_precos)
print(f"O maior elemento da lista eh {maior}")

# 4) Menor elemento da lista: funcao min
menor = min(lista_precos)
print(f"O menor elemento da lista eh {menor}")

# 5) Indice de um elemento da lista
elem = float(input("Digite um numero real para saber em qual indice ele esta na lista: "))

if (elem in lista_precos):
    indice = lista_precos.index(elem)
    print(f"O indice eh {indice}")
else:
    print("O numero nao pertence a lista")

