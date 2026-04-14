<<<<<<< HEAD
# Tratamento de Erros no Python

# Exemplo da soma de 2 numeros inteiros - SEM tratamento de erros

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

soma = num1 + num2
print(f"A soma dos numeros {num1} e {num2} eh: {soma}")


# Exemplo da soma COM tratamento de erros

try:
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))

    soma = num1 + num2
    print(f"A soma dos numeros {num1} e {num2} eh: {soma}")
except ValueError:
    print("Erro: Por favor, insira apenas numeros inteiros.")
else:
    soma = num1 + num2
    print(f"A soma dos numeros eh: {soma}")
finally:
=======
# Tratamento de Erros no Python

# Exemplo da soma de 2 numeros inteiros - SEM tratamento de erros

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

soma = num1 + num2
print(f"A soma dos numeros {num1} e {num2} eh: {soma}")


# Exemplo da soma COM tratamento de erros

try:
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))

    soma = num1 + num2
    print(f"A soma dos numeros {num1} e {num2} eh: {soma}")
except ValueError:
    print("Erro: Por favor, insira apenas numeros inteiros.")
else:
    soma = num1 + num2
    print(f"A soma dos numeros eh: {soma}")
finally:
>>>>>>> dce969be1322e2f1e5760a2a1b2ef33fd8f2fda2
    print("Fim do programa.")