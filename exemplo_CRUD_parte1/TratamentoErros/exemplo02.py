<<<<<<< HEAD
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
=======
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
>>>>>>> dce969be1322e2f1e5760a2a1b2ef33fd8f2fda2
        print("Operação concluída!")