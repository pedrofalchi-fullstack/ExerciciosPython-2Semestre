# Função que calcula soma de números definidos como parametros
def somar_numeros(num1, num2):
    soma = num1 + num2
    return(soma)

# Chamada da função somar_numeros
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

s = somar_numeros (n1,n2)

print(f"O resultado da soma é: {s}")

# Outra forma de chamar uma função com parametros
s = somar_numeros(num1=20,num2=45)
print(f"O valor da soma é : {s}")