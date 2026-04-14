import json
import requests


def main():
    lista_carros = []
    resp = 1

    while (resp == 1):
        print("1 - Inserir carro")
        print("2 - Alterar carro")
        print("3 - Excluir carro")
        print("4 - Exibir dados de um carro")
        print("5 - Exportar os dados para um arquivo json")
        print("6 - Importar os dados do arquivo json para a lista")
        print("7 - Gerar arquivo texto com os dados dos carros da marca Honda fabricados depois de 2018")
        print("8 - Buscar valor FIPE")
        opc = int(input("Digite a opcao desejada (1 a 8): "))

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
            codigo_exibir = int(input("Digite o codigo do carro que deseja exibir: "))
            indice = buscar_carro(lista_carros, codigo_exibir)
            if (indice != -1):
                exibir_carro(lista_carros, indice)
            else:
                print("Codigo inexistente!")
        elif (opc == 5):
            # Exportacao para um arquivo json
            exportar_arquivo_json(lista_carros)
        elif (opc == 6):
            # Importacao do arquivo json
            importar_arquivo_json(lista_carros)
        elif (opc == 7):
            # Arq. txt do relatorio
            gerar_arqtxt_relatorio(lista_carros)
        elif (opc == 8):
            marca = input("Digite a marca do carro: ")
            modelo = input("Digite o modelo do carro: ")
            ano = int(input("Digite o ano do carro: "))

            valor = buscar_valor_fipe(marca, modelo, ano)
            print(f"Valor FIPE: {valor}")
        else:
            print("Opcao invalida")

        resp = int(input("Deseja continuar (1-SIM/0-NAO)? "))

def buscar_valor_fipe(marca, modelo, ano):
    # end point para consultar o valor da tabela FIPE pela API (Fipe API)
    str_endpoint_marcas = "https://parallelum.com.br/fipe/api/v1/carros/marcas"

    # busca pela marca (requisição)
    requisicao_marcas = requests.get(str_endpoint_marcas)

    if(requisicao_marcas.status_code == 200):
        marcas = requisicao_marcas.json()

        id_marca = None

        for m in marcas:
            if(marca.lower() in m['nome'].lower()):
                id_marca = m['codigo']
                break

        if not id_marca:
            return "Marca não encontrada!"
        
    else:
        print("Requisição nao efetuada.")  


    str_endpoint_modelos = f"{str_endpoint_marcas}/{id_marca}/modelos"

    # busca por modelo (requisição)
    requisicao_modelos = requests.get(str_endpoint_modelos)

    if(requisicao_modelos.status_code == 200):  
        modelos = requisicao_modelos.json()['modelos']

        id_modelo = None

        for mod in modelos:
            if(modelo.lower() in mod['nome'].lower()):
                id_modelo = mod['codigo']
                break

        if not id_modelo:
            return "Marca não encontrada!"
        
    else:
        print("Requisição nao efetuada.") 



    # busca por anos
    str_endpoint_anos = f"{str_endpoint_marcas}/{id_marca}/modelos/{id_modelo}/anos"

    requisicao_anos = requests.get(str_endpoint_anos)

    if(requisicao_anos.status_code == 200):
        lista_anos = requisicao_anos.json()

        id_ano = None

        for a in lista_anos:
            if(str(ano) in a['nome']):
                id_ano = a['codigo']
                break

        if not id_ano:
            return "Marca não encontrada!"
        
    else:
        print("Requisição nao efetuada.")


    # buscar valor da tabela fipe
    endpoint_final = f"{str_endpoint_anos}/{id_ano}"

    requisicao_valor_fipe = requests.get(endpoint_final)

    if(requisicao_valor_fipe.status_code == 200):
        dados_carro = requisicao_valor_fipe.json()
        return (dados_carro['Valor'])
    
    else:
        return(0)




def gerar_arqtxt_relatorio(lista_carros):
    nome_arq = input("Digite o nome do arquivo texto com extensao .txt: ")
    if (len(lista_carros) > 0):
        for i in range(len(lista_carros)):
            if (lista_carros[i]['Marca'] == "Honda" and lista_carros[i]['Ano'] > 2018):
                str_carro = lista_carros[i]['Marca'] + "\t" + lista_carros[i]['Modelo'] + "\t" + str(lista_carros[i]['Ano']) + "\n"
                with open(nome_arq,"a",encoding = "utf-8") as arqCarros:
                    arqCarros.write(str_carro)
                    arqCarros.close()
    else:
        print("Nao existem carros cadastrados")


def exportar_arquivo_json(lista_carros):
    nome_arq = input("Digite o nome do arquivo json com extensao .json: ")
    if (len(lista_carros) > 0):
        with open(nome_arq,"w",encoding = "utf-8") as arqCarros:
            json.dump(lista_carros,arqCarros,ensure_ascii=False,indent="4")
        print("Arquivo json gravado com sucesso!")
    else:
        print("Nao existem funcionarios cadastrados")

def importar_arquivo_json(lista_carros):
    nome_arq = input("Digite o nome do arquivo json para recuperar os dados da lista: ")
    lista_carros.clear()
    with open(nome_arq,"r",encoding = "utf-8") as arqCarros:
        dados_arq = arqCarros.read()
        lista_dados_json = json.loads(dados_arq)
        for carro in lista_dados_json:
            lista_carros.append(carro)
    print("Dados importados com sucesso!")

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
            valor_fipe = buscar_valor_fipe(marca, modelo, ano)
            print(f"Valor FIPE: {valor_fipe}")
    except ValueError:
        print("Digite valores numericos para o codigo e ano")
    else:
        dados_carro = {
            'Codigo': codigo,
            'Marca': marca,
            'Modelo': modelo,
            'Ano': ano,
            'ValorFIPE': valor_fipe
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
        valor_fipe = buscar_valor_fipe(marca, modelo, ano)
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