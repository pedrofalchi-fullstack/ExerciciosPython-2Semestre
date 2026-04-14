'''
Escreva um programa em Python que faça um CRUD em uma lista de medicamentos de uma farmácia, os quais devem conter os seguintes dados: 

Código; 

Descrição;  

Indicação; 

Preço de compra; 

Preço de venda; 

 

Faça o tratamento de erros no processo de inserção e alteração. As operações deverão ser executadas até que o usuário digite uma opção de saída 0 (Deseja continuar (1-SIM / 0-NÃO). 

OBS: o programa deverá ter, obrigatoriamente, a função “main” e cada operação do CRUD deverá ser uma função. Na operação de inserção, faça a validação do código como se fosse uma chave primária. 
'''

def main():
    lista_medicamentos = []
    resp = 1

    while (resp == 1):
        print("1 - Inserir medicamento")
        print("2 - Alterar medicamento")
        print("3 - Excluir medicamento")
        print("4 - Exibir dados de um medicamento")
        opc = int(input("Digite a opcao desejada (1 a 4): "))

        if (opc == 1):
            # Insercao
            inserir_medicamento(lista_medicamentos)
        elif (opc == 2):
            # Alteracao
            codigo_alterar = int(input("Digite o codigo do medicamento que deseja alterar: "))
            indice = buscar_medicamento(lista_medicamentos, codigo_alterar)
            if (indice != -1):
                alterar_medicamento(lista_medicamentos, indice)
            else:
                print("Codigo inexistente!")
        elif (opc == 3):
            # Exclusao
            codigo_excluir = int(input("Digite o codigo do medicamento que deseja alterar: "))
            indice = buscar_medicamento(lista_medicamentos, codigo_excluir)
            if (indice != -1):
                excluir_medicamento(lista_medicamentos, indice)
            else:
                print("Codigo inexistente!")
        elif (opc == 4):
            # Exibir dados
            codigo_exibir = int(input("Digite o codigo do medicamento que deseja alterar: "))
            indice = buscar_medicamento(lista_medicamentos, codigo_exibir)
            if (indice != -1):
                exibir_medicamento(lista_medicamentos, indice)
            else:
                print("Codigo inexistente!")
        else:
            print("Opcao invalida")

        resp = int(input("Deseja continuar (1-SIM/0-NAO)? "))


def buscar_medicamento(lista_medicamentos, codigo):
    indice = -1
    for i in range(len(lista_medicamentos)):
        if (lista_medicamentos[i]['Codigo'] == codigo):
            indice = i
    return (indice)


def inserir_medicamento(lista_medicamentos):
    try:
        codigo = int(input("Digite o codigo do medicamento: "))
        indice = buscar_medicamento(lista_medicamentos, codigo)
        while (indice != -1):
            codigo = int(input("Codigo ja existente. Digite outro codigo do medicamento: "))
            indice = buscar_medicamento(lista_medicamentos, codigo)
        descr = input("Digite a descricao do medicamento: ")
        indicacao= input("Digite a indicacao do medicamento: ")
        preco_compra = float(input("Digite o preco de compra do medicamento: "))
        preco_venda = float(input("Digite o preco de venda do medicamento: "))
    except ValueError:
        print("Digite valores numericos para o codigo, preco de compra e preco de venda")
    else:
        dados_medicamento = {
            'Codigo': codigo,
            'Descricao': descr,
            'Indicacao': indicacao,
            'Preco_compra': preco_compra,
            'Preco_venda': preco_venda
        }
        lista_medicamentos.append(dados_medicamento)
        print("Dados inseridos com sucesso!")


def alterar_medicamento(lista_medicamentos, indice):
    try:
        print(f"Descricao: {lista_medicamentos[indice]['Descricao']}")
        nova_descr = input("Digite a nova descricao do medicamento: ")
        print(f"Indicacao: {lista_medicamentos[indice]['Indicacao']}")
        nova_indicacao = input("Digite a nova indicacao do medicamento: ")
        print(f"Preco de compra: {lista_medicamentos[indice]['Preco_compra']}")
        novo_preco_compra = float(input("Digite o novo preco de compra do medicamento: "))
        print(f"Preco de venda: {lista_medicamentos[indice]['Preco_venda']}")
        novo_preco_venda = float(input("Digite o novo preco de venda do medicamento: "))
    except ValueError:
        print("Digite valores numericos para o preco de compra e preco de venda")
    else:
        lista_medicamentos[indice]['Descricao'] = nova_descr
        lista_medicamentos[indice]['Indicao'] = nova_indicacao
        lista_medicamentos[indice]['Preco_compra'] = novo_preco_compra
        lista_medicamentos[indice]['Preco_venda'] = novo_preco_venda
        print("Dados alterados com sucesso!")


def excluir_medicamento(lista_medicamentos, indice):
    lista_medicamentos.pop(indice)
    print("medicamento excluido com sucesso!")


def exibir_medicamento(lista_medicamentos, indice):
    for chave, valor in lista_medicamentos[indice].items():
        print(f"{chave}: {valor}")


if (__name__ == "__main__"):
    main()