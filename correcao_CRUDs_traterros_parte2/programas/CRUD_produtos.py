'''
Crie um programa em Python com o menu abaixo para realizar as operações (CRUD) em uma lista de produtos em estoque (lista de dicionários) de uma determinada empresa.

1-Incluir
2-Alterar
3-Exibir
4-Excluir



Os dados a serem armazenados devem ser os seguintes: descrição, quantidade, marca e valor. Na opção de alteração dos dados, permita que o usuário altere todos os campos, exceto a descrição. As operações deverão ser executadas até que o usuário digite uma opção de saída 0 (Deseja continuar (1-SIM / 0-NÃO). Quando o usuário não desejar mais efetuar as operações, faça um relatório de todos os produtos de uma determinada marca escolhida pelo usuário cuja quantidade em estoque seja superior a 50 unidades.
'''
lista_produtos = []

resp = 1 # 1-SIM 0-NAO

while (resp == 1):
    print("1 - Inserir um produto")
    print("2 - Alterar um produto")
    print("3 - Excluir um produto")
    print("4 - Exibir um produto")
    print("5 - Relatorio de todos os produtos cuja quantidade em estoque seja superior a 50 unidades")
    opc = int(input("Digite a opcao desejada (1 a 5): "))

    if (opc == 1):
        # Insercao de um produto
        try:
            descricao = input("Digite a descricao do produto: ")
            marca = input("Digite a marca do produto: ")
            qtde = int(input("Digite a quantidade do produto: "))
            valor = float(input("Digite o valor do produto: "))
        except ValueError:
            print("Digite valores numericos para a quantidade e o valor!")
        else:
            dados_produto = {
                'Descricao':descricao,
                'Marca':marca,
                'Quantidade':qtde,
                'Valor':valor
            }

            lista_produtos.append(dados_produto)
            print("Dados inseridos com sucesso!")
    elif (opc == 2):
        # Alteracao de um produto
        descr_alterar = input("Digite a descricao do produto que deseja alterar: ")
        indice = -1
        for i in range(len(lista_produtos)):
            if (lista_produtos[i]['Descricao'] == descr_alterar):
                indice = i
        if (indice != -1):
            try:
                print(f"Marca: {lista_produtos[indice]['Marca']}")
                nova_marca = input("Digite a nova marca do produto: ")
                print(f"Quantidade: {lista_produtos[indice]['Quantidade']}")
                nova_qtde = int(input("Digite a nova quantidade do produto: "))
                print(f"Valor: {lista_produtos[indice]['Valor']}")
                novo_valor = float(input("Digite a novo valor do produto: "))
            except ValueError:
                print("Digite valores numericos para a quantidade e o valor!")
            else:
                lista_produtos[indice]['Marca'] = nova_marca
                lista_produtos[indice]['Quantidade'] = nova_qtde
                lista_produtos[indice]['Valor'] = novo_valor
                print("Dados alterados com sucesso!")
        else:
            print("Nao existe produto com essa descricao! ")
    elif (opc == 3):
        # Exclusao de um produto
        descr_excluir = input("Digite a descricao do produto que deseja excluir: ")
        indice = -1
        for i in range(len(lista_produtos)):
            if (lista_produtos[i]['Descricao'] == descr_excluir):
                indice = i
        if (indice != -1):
            lista_produtos.pop(indice)
            print("Produto excluido com sucesso!")
        else:
            print("Nao existe produto com essa descricao! ")
    elif (opc == 4):
        # Exibicao de um produto
        descr_exibir = input("Digite a descricao do produto que deseja exibir: ")
        indice = -1
        for i in range(len(lista_produtos)):
            if (lista_produtos[i]['Descricao'] == descr_exibir):
                indice = i
        if (indice != -1):
            for chave, valor in lista_produtos[indice].items():
                print(f"{chave}: {valor}")
        else:
            print("Nao existe produto com essa descricao! ")
    elif (opc == 5):
        # Relatorio de todos os produtos cuja quantidade em estoque seja superior a 50 unidades
        for i in range(len(lista_produtos)):
            if (lista_produtos[i]['Quantidade'] > 50):
                for chave, valor in lista_produtos[i].items():
                    print(f"{chave}: {valor}")
                print("-------------------------------------------")
    else:
        print("Opcao invalida! ")

    resp = int(input("Deseja continuar (1-SIM / 0-NAO)? "))

