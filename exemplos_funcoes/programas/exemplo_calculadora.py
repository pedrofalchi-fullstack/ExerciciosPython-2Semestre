def main():
    resp  = 1
    while (resp == 1):
        print("1 - Somar numeros")
        print("2 - Subtrair numeros")
        print("3 - Multiplicar numeros")
        print("4 - Dividir numeros")
        opc = int(input("Digite a opcao desejada (1 a 4): "))

        if (opc == 1):
            n1, n2 = ler_numeros()
            print(f"A soma dos 2 numeros eh {somar_numeros (n1, n2)}")
        elif (opc == 2):
            n1, n2 = ler_numeros()
            print(f"A subtracao dos 2 numeros eh {subtrair_numeros(n1, n2)}")
        elif (opc == 3):
            n1, n2 = ler_numeros()
            print(f"A multiplicao dos 2 numeros eh {multiplicar_numeros(n1, n2)}")
        elif (opc == 4):
            n1, n2 = ler_numeros()
            print(f"A divisao dos 2 numeros eh {dividir_numeros(n1, n2)}")
        else:
            print("Opcao invalida")

        resp = int(input("Deseja continuar (1-SIM / 0-NAO)? "))

def ler_numeros():
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))
    return(num1,num2)

def somar_numeros (num1, num2):
    soma = num1 + num2
    return(soma)

def subtrair_numeros (num1, num2):
    sub = num1 - num2
    return (sub)

def multiplicar_numeros (num1, num2):
    mult = num1 * num2
    return (mult)

def dividir_numeros (num1, num2):
    div = num1 / num2
    return (div)

# Chamada da funcao main
if (__name__ == "__main__"):
    main()