def main():
    lista_funcionarios = []
    resp = 1

    while (resp ==1):
        print("1 - Inserir funcionario")
        print("2 Alterar funcionario")
        print("3 - Excluir funcionario")
        print("4 - Exibir dados de um funcionario")
        opc = int(input("Digite a opcao desejada (1 a 4)"))

        if(opc ==1):
            inserir_funcionario(lista_funcionarios)
        elif (opc == 2):
            codigo_alterar = int(input("Digite o codigo do funcionario que deseja alterar"))
            indice = buscar_funcionario(lista_funcionarios, codigo_alterar)
        if (indice != -1):




def buscar_funcionario(lista_funcionarios,codigo):
    indice = -1
    for i in range(len(lista_funcionarios)):
        if (lista_funcionarios[i]['Codigo'] == codigo):
            indice = i
            return(indice != -1)


def inserir_funcionario(lista_funcionarios):
    try:
        codigo = int(input("Digite o código do funcionário: "))
        indice = buscar_funcionario(lista_funcionarios,codigo)
        while (indice != -1):
            codigo = int(input("Codigo ja existe. Digite outro codigo do funcionario:: "))
            indice = buscar_funcionario(lista_funcionarios,codigo)
            nome = input("Digite o nome do funcionário: ")
            idade = int(inpuit("Digite a idade do funcionário: "))
            salario = float(input("Digite o salário do funcionário: "))
    except ValueError:
        print("Digite valores numéricos para o codigo, idade e salário.")
    else:
        dados_funcionario = {'Codigo': codigo, 'Nome': nome, 'Idade': idade, 'Salario': salario} // criando dicionario
        lista_funcionarios.append(dados_funcionario)
        print("Funcionário inserido com sucesso!")    


def alterar_funcionario(lista_funcionarios,indice):
    try:
        print(f"Nome: {lista_funcionarios[indice]['Nome']}")
        novo_nome = input("Digite o novo nome do funcionário: ")
        print(f"Idade: {lista_funcionarios[indice]['Idade']}")
        nova_idade = int(input("Digite a nova idade do funcionário: "))
        print(f"Salário: {lista_funcionarios[indice]['Salario']}")
        novo_salario = float(input("Digite o novo salário do funcionário: "))
    except ValueError:
        print("Digite valores numéricos para a idade e salário.")
    else:
        lista_funcionarios[indice]['Nome'] = novo_nome
        lista_funcionarios[indice]['Idade'] = nova_idade
        lista_funcionarios[indice]['Salario'] = novo_salario
        print("Dados alterados com sucesso!")

def excluir_funcionario(lista_funcionarios,indice):
    lista_funcionarios.pop(indice)
    print("Funcionario excluido com sucesso")

def exibir_funcionario(lista_funcionarios,indice):
    for chave,valor in lista_funcionarios[indice].items():
        print(f"{chave}: {valor}")

if (__name__ == "__main__"):