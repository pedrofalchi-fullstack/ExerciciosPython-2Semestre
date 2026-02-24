# Lista de Dicionarios
# Criar uma lista para armazenar os dados de 5 alunos

lista_alunos = []

for i in range(5):
    rm = int(input("Digite o RM do aluno: "))
    nome = input("Digite o nome do aluno: ")
    curso = input("Digite o curso do aluno: ")
    mensalidade = float(input("Digite a mensalidade do curso do aluno: "))
    cpf = input("Digite o CPF do aluno: ")

    dados_aluno = {
        'RM_aluno':rm,
        'Nome_aluno':nome,
        'Curso_aluno':curso,
        'Mensalidade_aluno':mensalidade,
        'CPF_aluno':cpf
    }

    lista_alunos.append(dados_aluno)

    # Exibir a lista de dicionarios de forma mais simples
    print(lista_alunos)

    # Exibir lista de dicionarios com dados de cada aluno separadamente
    for i in range(5):
        for chave, valor in lista_alunos[i].items():
            print(f"{chave}: {valor}")
        print("--------------------------------------------------")