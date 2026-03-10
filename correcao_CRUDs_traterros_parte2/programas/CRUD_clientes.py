'''
Crie um programa em Python com o menu abaixo para realizar as operações (CRUD) em uma lista de clientes (lista de dicionários) de uma determinada loja.

1-Incluir
2-Alterar
3-Exibir
4-Excluir

Os dados a serem armazenados devem ser os seguintes: nome, CPF, idade, endereço e limite de crédito. Na opção de alteração dos dados, permita que o usuário altere todos os campos, exceto o nome. As operações deverão ser executadas até que o usuário digite uma opção de saída 0 (Deseja continuar (1-SIM / 0-NÃO). Quando o usuário não desejar mais efetuar as operações, faça um relatório de todos os clientes cujo limite de crédito é maior do que 1500,00.
'''
lista_clientes = []

resp = 1 # 1-SIM 0-NAO

while (resp == 1):
    print("1 - Inserir um cliente")
    print("2 - Alterar um cliente")
    print("3 - Excluir um cliente")
    print("4 - Exibir um cliente")
    print("5 - Relatório de todos os clientes cujo limite de crédito é maior do que 1500,00")
    opc = int(input("Digite a opcao desejada (1 a 5): "))

    if (opc == 1):
        # insercao de um cliente
        try:
            nome = input("Digite o nome do cliente: ")
            cpf = input("Digite o CPF do cliente: ")
            idade = int(input("Digite a idade do cliente: "))
            endereco = input("Digite o endereco do cliente: ")
            limite_credito = float(input("Digite o limite de credito do cliente: "))
        except ValueError:
            print("Digite valores numericos para a idade e limite de credito!")
        else:
            dados_cliente = {
                'Nome':nome,
                'CPF':cpf,
                'Idade':idade,
                'Endereco':endereco,
                'Limite_credito':limite_credito
            }
            lista_clientes.append(dados_cliente)
            print("Dados inseridos com sucesso!")
    elif (opc == 2):
        # alteracao dos dados de um cliente
        nome_alterar = input("Digite o nome do cliente que deseja alterar os dados: ")
        # busca do cliente pelo nome
        indice = -1
        for i in range(len(lista_clientes)):
            if (lista_clientes[i]['Nome'] == nome_alterar):
                indice = i
        if (indice != -1): # encontrou o nome na lista
            try:
                print(f"CPF: {lista_clientes[indice]['CPF']}")
                novo_cpf = input("Digite o novo CPF: ")
                print(f"Idade: {lista_clientes[indice]['Idade']}")
                nova_idade = int(input("Digite a nova idade: "))
                print(f"Endereco: {lista_clientes[indice]['Endereco']}")
                novo_endereco = input("Digite o novo endereco: ")
                print(f"Limite de Credito: {lista_clientes[indice]['Limite_credito']}")
                novo_limite_credito = float(input("Digite o novo limite de credito: "))
            except ValueError:
                print("Digite valores numericos para a idade e limite de credito!")
            else:
                lista_clientes[indice]['CPF'] = novo_cpf
                lista_clientes[indice]['Idade'] = nova_idade
                lista_clientes[indice]['Endereco'] = novo_endereco
                lista_clientes[indice]['Limite_credito'] = novo_limite_credito
                print("Dados alterados com sucesso!")
        else:
            print("O nome nao esta cadastrado!")
    elif (opc == 3):
        # exclusao de um cliente
        nome_excluir = input("Digite o nome do cliente que deseja excluir os dados: ")
        # busca do cliente pelo nome
        indice = -1
        for i in range(len(lista_clientes)):
            if (lista_clientes[i]['Nome'] == nome_excluir):
                indice = i
        if (indice != -1):  # encontrou o nome na lista
            lista_clientes.pop(indice)
            print("Cliente excluido com sucesso!")
        else:
            print("O nome nao esta cadastrado!")
    elif (opc == 4):
        # exibicao dos dados de um cliente
        nome_exibir = input("Digite o nome do cliente que deseja exibir os dados: ")
        # busca do cliente pelo nome
        indice = -1
        for i in range(len(lista_clientes)):
            if (lista_clientes[i]['Nome'] == nome_exibir):
                indice = i
        if (indice != -1):  # encontrou o nome na lista
            for chave,valor in lista_clientes[indice].items():
                print(f"{chave}: {valor}")
        else:
            print("O nome nao esta cadastrado!")
    elif (opc == 5):
        # Relatorio dos clientes cujo limite de credito é maior do que 1500
        for i in range(len(lista_clientes)):
            if (lista_clientes[i]['Limite_credito'] > 1500):
                for chave,valor in lista_clientes[i].items():
                    print(f"{chave}: {valor}")
                print("--------------------------------------------")
    else:
        print("Opcao invalida!")

    resp = int(input("Deseja continuar (1-SIM / 0-NAO)? "))

