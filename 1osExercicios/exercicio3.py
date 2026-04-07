lista_notas = []
qtde_notas_acima_media = 0
qtde_notas_abaixo_7 = 0

nota = float(input("digite a nota do aluno"))

while (nota != -1):
    if (nota >= 0 and nota <= 10):
        lista_notas.append(nota)
    else:
        print("A nota deve estar entre 0 e 10")

    nota = float(input("Digite a nota do aluno: "))


tamanho_lista = len(lista_notas)
print(f"Quantidade de notas (valores lidos): {tamanho_lista}")

soma_notas = sum(lista_notas)
print(f"A soma das notas é: {soma_notas:.2f}")

media_notas = soma_notas / tamanho_lista
print(f"A média das notas é: {media_notas:.2f}")

for i in range(tamanho_lista):
    if (lista_notas[i] > media_notas):
        qtde_notas_acima_media+=1 # qtde_notas_acima_media = qtde_notas_acima_media + 1

    if (lista_notas[i] < 7):
        qtde_notas_abaixo_7+=1

print(f"Quantidade de notas acima da média: {qtde_notas_acima_media}")
print(f"Quantidade de notas abaixo de sete: {qtde_notas_abaixo_7}")