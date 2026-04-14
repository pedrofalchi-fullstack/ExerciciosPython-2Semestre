# Revisao sobre estruturas de repeticao e listas

# for

# Exemplo 1: exibir todos os numeros inteiros de 1 a 20
for cont in range(1,21):
    print(cont)

print("Terminou")

# Exemplo 2: calcular o somatorio dos numeros de 2 ate 50
soma = 0

for cont in range(2,51):
    soma = soma + cont

print(f"O somatorio de 2 ate 50 eh {soma}")

# Exemplo 3: calcular o somatorio de 10 numeros digitados pelo usuario
soma = 0

for cont in range(10): # cont vai variar de 0 a 9
    num = int(input("Digite um numero inteiro: "))
    soma = soma + num

print(f"O somatorio dos numeros digitados eh {soma}")

# exibir somente os numeros pares de 2 ate 30
for cont in range(2,31,2):
    print(cont)