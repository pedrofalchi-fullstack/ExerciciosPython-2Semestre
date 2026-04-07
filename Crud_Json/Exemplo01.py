import json

def main():
    lista_alunos = []

opcao = 1

while (opcao != 7):
    print("1 - Inserir um aluno")
    print("2 - Alterar um aluno")
    print("3 - Excluir um aluno")
    print("4 - Exibir um aluno")
    print("5 - Exportar dados para um arquivo Json")
    print("6 - Importar dados de um arquivo Json para Lista")
    print("7 - Sair")
    opcao = int(input("Digite a opcao desejada (1 a 5): "))

    if (opcao >= 1 and opcao <= 6):
        # Insercao de um aluno
        if (opcao == 1):
            try:
                rm = int(input("RM: "))
                nome = input("Nome: ")
                curso = input("Curso: ")
                mensalidade = float(input("Mensalidade: "))
            except ValueError:
                print("Digite valores numericos para o rm e a mensalidade!")
            else:
                dados_aluno = {
                    'RM':rm,
                    'Nome':nome,
                    'Curso':curso,
                    'Mensalidade':mensalidade
                }

                lista_alunos.append(dados_aluno)
            finally:
                print("Operacao concluida!")
        elif (opcao == 2):
            # Alteracao de um aluno
            rm_alterar = int(input("Digite o RM do aluno que deseja alterar: "))
            indice = -1
            for i in range(len(lista_alunos)):
                if (lista_alunos[i]['RM'] == rm_alterar):
                    indice = i
            if (indice != -1):
                try:
                    print(f"Nome: {lista_alunos[indice]['Nome']}")
                    nome = input("Digite o novo nome: ")
                    print(f"Curso: {lista_alunos[indice]['Curso']}")
                    curso = input("Digite o novo curso: ")
                    print(f"Mensalidade: {lista_alunos[indice]['Mensalidade']}")
                    mensalidade = float(input("Digite a nova mensalidade: "))
                except ValueError:
                    print("Digite um valor numerico para a mensalidade!")
                else:
                    lista_alunos[indice]['Nome'] = nome
                    lista_alunos[indice]['Curso'] = curso
                    lista_alunos[indice]['Mensalidade'] = mensalidade
                finally:
                    print("Operacao concluida! ")
            else:
                print("RM nao encontrado")
        elif (opcao == 3):
            # Remocao de um aluno
            rm_excluir = int(input("Digite o RM do aluno que deseja excluir: "))
            indice = -1
            for i in range(len(lista_alunos)):
                if (lista_alunos[i]['RM'] == rm_excluir):
                    indice = i
            if (indice != -1):
                lista_alunos.pop(indice)
            else:
                print("RM nao encontrado")
        else:
            # Exibicao de um aluno
            rm_exibir = int(input("Digite o RM do aluno que deseja exibir: "))
            indice = -1
            for i in range(len(lista_alunos)):
                if (lista_alunos[i]['RM'] == rm_exibir):
                    indice = i
            if (indice != -1):
                for chave,valor in lista_alunos[indice].items():
                    print(f"{chave}: {valor}")
            else:
                print("RM nao encontrado")
        elif (opcao == 5):
                # Exportação para um arquivo json
            exportar_arquivo_json(lista_alunos)
        elif (opcao == 6):
            #Importar para um arquivo json
    else:
        print("Opcao invalida!")