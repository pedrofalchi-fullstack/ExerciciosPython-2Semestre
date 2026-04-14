'''
Escreva um programa em Python que faça um CRUD em uma lista de carros, os quais devem conter os seguintes dados: 

Código; 

Marca; 

Modelo; 

Ano; 

Faça o tratamento de erros no processo de inserção e alteração. As operações deverão ser executadas até que o usuário digite uma opção de saída 0 (Deseja continuar (1-SIM / 0-NÃO). 

OBS: o programa deverá ter, obrigatoriamente, a função “main” e cada operação do CRUD deverá ser uma função. Na operação de inserção, faça a validação do código como se fosse uma chave primária. 
'''

def main():
    lista_carros = []
    resp = 1

    while (resp == 1):
        print("1 - Inserir carro")
        print("2 - Alterar carro")
        print("3 - Excluir carro")
        print("4 - Exibir dados de um carro")
        opc = int(input("Digite a opcao desejada (1 a 4): "))

        if (opc == 1):
            # Insercao
            inserir_carro(lista_carros)
        elif (opc == 2):
            # Alteracao
            codigo_alterar = int(input("Digite o codigo do carro que deseja alterar: "))
            indice = buscar_carro(lista_carros, codigo_alterar)
            if (indice != -1):
                alterar_carro(lista_carros, indice)
            else:
                print("Codigo inexistente!")
        elif (opc == 3):
            # Exclusao
            codigo_excluir = int(input("Digite o codigo do carro que deseja alterar: "))
            indice = buscar_carro(lista_carros, codigo_excluir)
            if (indice != -1):
                excluir_carro(lista_carros, indice)
            else:
                print("Codigo inexistente!")
        elif (opc == 4):
            # Exibir dados
            codigo_exibir = int(input("Digite o codigo do carro que deseja alterar: "))
            indice = buscar_carro(lista_carros, codigo_exibir)
            if (indice != -1):
                exibir_carro(lista_carros, indice)
            else:
                print("Codigo inexistente!")
        else:
            print("Opcao invalida")

        resp = int(input("Deseja continuar (1-SIM/0-NAO)? "))


def buscar_carro(lista_carros, codigo):
    indice = -1
    for i in range(len(lista_carros)):
        if (lista_carros[i]['Codigo'] == codigo):
            indice = i
    return (indice)


def inserir_carro(lista_carros):
    try:
        codigo = int(input("Digite o codigo do carro: "))
        indice = buscar_carro(lista_carros, codigo)
        while (indice != -1):
            codigo = int(input("Codigo ja existente. Digite outro codigo do carro: "))
            indice = buscar_carro(lista_carros, codigo)
        marca = input("Digite a marca do carro: ")
        modelo = input("Digite o modelo do carro: ")
        ano = int(input("Digite o ano do carro: "))
    except ValueError:
        print("Digite valores numericos para o codigo e ano")
    else:
        dados_carro = {
            'Codigo': codigo,
            'Marca': marca,
            'Modelo': modelo,
            'Ano': ano
        }
        lista_carros.append(dados_carro)
        print("Dados inseridos com sucesso!")


def alterar_carro(lista_carros, indice):
    try:
        print(f"Marca: {lista_carros[indice]['Marca']}")
        nova_marca = input("Digite a nova marca do carro: ")
        print(f"Modelo: {lista_carros[indice]['Modelo']}")
        novo_modelo = input("Digite o novo modelo do carro: ")
        print(f"Ano: {lista_carros[indice]['Ano']}")
        novo_ano = int(input("Digite o novo ano do carro: "))
    except ValueError:
        print("Digite valores numericos para o ano")
    else:
        lista_carros[indice]['Modelo'] = novo_modelo
        lista_carros[indice]['Marca'] = nova_marca
        lista_carros[indice]['Ano'] = novo_ano
        print("Dados alterados com sucesso!")


def excluir_carro(lista_carros, indice):
    lista_carros.pop(indice)
    print("carro excluido com sucesso!")


def exibir_carro(lista_carros, indice):
    for chave, valor in lista_carros[indice].items():
        print(f"{chave}: {valor}")


if (__name__ == "__main__"):
    main()