# Programa que faz a divisão de dois números inteiros com tratamento de erros

acertou = 1

while (acertou == 1):

    try:
        num1 = int(input("Digite o primeiro numero: "))
        num2 = int(input("Digite o segundo numero: "))
        divisao = num1 / num2
    except ValueError:
        print("Erro: Por favor, insira apenas numeros inteiros.")
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero.")
    else:
        print(f"A divisão dos numeros {num1} e {num2} eh: {divisao}")
        acertou = 0
    finally:
        print("Operação concluída!")