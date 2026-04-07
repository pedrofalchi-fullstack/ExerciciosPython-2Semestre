def main():
    resp = 1
    while resp == 1:
        print("1 - Somar números")
        print("2 - Subtrair números")
        print("3 - Multiplicar números")
        print("4 - Dividir números")
        opc = int(input("Digite a opção desejada (1 a 4): "))

        if (opc == 1):
            n1, n2 = ler_numeros()
            print(f"A soma dos 2 números é: {somar_numeros(n1,n2)}")
        elif (opc == 2):
            n1, n2 = ler_numeros()
            print(f"A subtração dos 2 números é: {subtrair_numeros(n1,n2)}")
        elif (opc == 3):
            n1, n2 = ler_numeros()
            print(f"A multiplicação dos 2 números é: {multiplicar_numeros(n1,n2)}")
        elif (opc == 4):
            n1, n2 = ler_numeros()
            print(f"A divisão dos 2 números é: {dividir_numeros(n1,n2)}")
        else:
            print("Opção inválida!")

        resp = int(input("Deseja realizar outra operação? (1 - Sim / 0 - Não): "))





def ler_numeros():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    return (num1,num2)

def somar_numeros(num1,num2):
    soma = num1 + num2
    return(soma)

def subtrair_numeros(num1,num2):
    sub = num1 - num2
    return(sub)

def multiplicar_numeros(num1,num2):
    mult = num1 * num2
    return(mult)

def dividir_numeros(num1,num2):
    div = num1 / num2
    return(div)

# Chamada de função main
if (__name__ == "__main__"):
    main()