# Funcao que calcula soma de numeros definidos como parametros
def somar_numeros (num1, num2):
    soma = num1 + num2
    return(soma)

# Chamada da funcao somar_numeros
n1 = int(input("Digite o primeiro numero para somar: "))
n2 = int(input("Digite o segundo numero para somar: "))

s = somar_numeros (n1,n2)

print(f"O valor da soma eh {s}")

# Outra forma de chamar uma funcao com parametros
s = somar_numeros(20,45)
print(f"O valor da soma eh {s}")

