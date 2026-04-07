import sys

def main():
    if (len(sys.argv) == 3):
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        print(f"A soma dos 2 numeros é {calcular_soma(num1,num2)}")
    else:print("Número de argumentos inválidos")



def calcular_soma(num1,num2):
    soma = num1 + num2
    return(soma)

if (__name__ == "__main__"):
    main()