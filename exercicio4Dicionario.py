# Dicionários em Python

dicionario_aluno = {
    'RM':2111445, # item do dicionário: composto por chave e valor
    #chave:valor
    'Nome_aluno':"João da Silva",
    'Curso':"TDS",
    'Mensalidade':1200
}

print(dicionario_aluno)

# Exibir o curso do aluno
print(f"Curso do aluno: {dicionario_aluno['Curso']}")

# Exibir a mensalidade do aluno:
print(f"Mensalidade do aluno: {dicionario_aluno['Mensalidade']}")

# Inserir outro item no dicionario
dicionario_aluno['CPF_aluno'] = "2345678-30"

print(dicionario_aluno)


# Funcao para acessar os itens do dicionario separadamente: items
print(dicionario_aluno.items())

# Exibir item por item em linhas separadas 
for chave,valor in dicionario_aluno.items():
    print(f"{chave}: {valor}")