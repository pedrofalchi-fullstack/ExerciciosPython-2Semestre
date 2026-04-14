
listaAlunos = []

for i in range(1):
    rm = int(input("digite o rm: "))
    nome = input("digite o nome: ")
    curso = input("digite o cusro: ")
    mensalidade = float(input("digite o mesalidade: "))
    cpf = input("digite o cpf: ")

    dadosAluno = {
        'RM': rm,
        'Nome': nome,
        'Curso': curso,
        'Mensalidade': mensalidade,
        'CPF': cpf,
    }
    listaAlunos.append(dadosAluno)
print(listaAlunos)

for i in range(1):
    for chave, valor in listaAlunos[i].items():
        print(f'{chave} : {valor}')