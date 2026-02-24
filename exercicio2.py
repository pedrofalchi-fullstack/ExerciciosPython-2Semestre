'''Faça um programa em Python que peça as 3 notas de 10 alunos, calcule e armazene em uma lista a média de cada aluno. 
Em seguida, imprima o número de alunos com média maior ou igual a 7.0
'''

# criando uma lista vazia
lista_medias = []

qtde_maior_igual_7 = 0

for i in range(10): # i vai variar de 0 a 9
    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))
    nota3 = float(input("Digite a terceira nota do aluno: "))
    media = (nota1 + nota2 + nota3) / 3
    lista_medias.append(media)

# percorrer a lista para contar os alunos que tiveram media maior ou igual a 7
for i in range(10):
    if (lista_medias[i] >= 7):
        qtde_maior_igual_7 = qtde_maior_igual_7 + 1

print(f"{qtde_maior_igual_7} alunos tiveram media maior ou igual a 7")
