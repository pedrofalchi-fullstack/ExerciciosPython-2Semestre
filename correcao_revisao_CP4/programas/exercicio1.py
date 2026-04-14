'''
1. Escreva um programa em Python que faça um CRUD em uma lista de dicionários, os quais devem conter os seguintes dados:

Código

Nome do funcionário

Idade do funcionário

Salário do funcionário

Faça o tratamento de erros no processo de inserção e alteração. As operações deverão ser executadas até que o usuário digite uma opção de saída 0 (Deseja continuar (1-SIM / 0-NÃO).

OBS: o programa deverá ter, obrigatoriamente, a função “main” e cada operação do CRUD deverá ser uma função. Na operação de inserção, faça a validação do código como se fosse uma chave primária.
'''

def main():
    lista_funcionarios = []
    resp = 1

    while (resp == 1):
        print("1 - Inserir funcionario")
        print("2 - Alterar funcionario")
        print("3 - Excluir funcionario")
        print("4 - Exibir dados de um funcionario")
        opc = int(input("Digite a opcao desejada (1 a 4): "))

        if (opc == 1):
            # Insercao
            inserir_funcionario(lista_funcionarios)
        elif (opc == 2):
            # Alteracao
            codigo_alterar = int(input("Digite o codigo do funcionario que deseja alterar: "))
            indice = buscar_funcionario(lista_funcionarios,codigo_alterar)
            if (indice != -1):
                alterar_funcionario(lista_funcionarios, indice)
            else:
                print("Codigo inexistente!")
        elif (opc == 3):
            # Exclusao
            codigo_excluir = int(input("Digite o codigo do funcionario que deseja alterar: "))
            indice = buscar_funcionario(lista_funcionarios, codigo_excluir)
            if (indice != -1):
                excluir_funcionario(lista_funcionarios, indice)
            else:
                print("Codigo inexistente!")
        elif (opc == 4):
            # Exibir dados
            codigo_exibir = int(input("Digite o codigo do funcionario que deseja alterar: "))
            indice = buscar_funcionario(lista_funcionarios, codigo_exibir)
            if (indice != -1):
                exibir_funcionario(lista_funcionarios, indice)
            else:
                print("Codigo inexistente!")
        else:
            print("Opcao invalida")

        resp = int(input("Deseja continuar (1-SIM/0-NAO)? "))

def buscar_funcionario(lista_funcionarios,codigo):
    indice = -1
    for i in range(len(lista_funcionarios)):
        if (lista_funcionarios[i]['Codigo'] == codigo):
            indice = i
    return(indice)


def inserir_funcionario(lista_funcionarios):
    try:
        codigo = int(input("Digite o codigo do funcionario: "))
        indice = buscar_funcionario(lista_funcionarios,codigo)
        while (indice != -1):
            codigo = int(input("Codigo ja existente. Digite outro codigo do funcionario: "))
            indice = buscar_funcionario(lista_funcionarios, codigo)
        nome = input("Digite o nome do funcionario: ")
        idade = int(input("Digite a idade do funcionario: "))
        salario = float(input("Digite o salario do funcionario: "))
    except ValueError:
        print("Digite valores numericos para o codigo, idade e salario")
    else:
        dados_funcionario = {
            'Codigo':codigo,
            'Nome':nome,
            'Idade':idade,
            'Salario':salario
        }
        lista_funcionarios.append(dados_funcionario)
        print("Dados inseridos com sucesso!")

def alterar_funcionario(lista_funcionarios,indice):
    try:
        print(f"Nome: {lista_funcionarios[indice]['Nome']}")
        novo_nome = input("Digite o novo nome do funcionario: ")
        print(f"Idade: {lista_funcionarios[indice]['Idade']}")
        nova_idade = int(input("Digite o nova idade do funcionario: "))
        print(f"Salario: {lista_funcionarios[indice]['Salario']}")
        novo_salario = float(input("Digite o novo salario do funcionario: "))
    except ValueError:
        print("Digite valores numericos para idade e salario")
    else:
        lista_funcionarios[indice]['Nome'] = novo_nome
        lista_funcionarios[indice]['Idade'] = nova_idade
        lista_funcionarios[indice]['Salario'] = novo_salario
        print("Dados alterados com sucesso!")

def excluir_funcionario(lista_funcionarios,indice):
    lista_funcionarios.pop(indice)
    print("Funcionario excluido com sucesso!")

def exibir_funcionario(lista_funcionarios,indice):
    for chave,valor in lista_funcionarios[indice].items():
        print(f"{chave}: {valor}")

if (__name__ == "__main__"):
    main()
