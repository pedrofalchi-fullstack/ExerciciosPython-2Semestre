numeros = [1,2,3,4,5,6,7,8,9,0]
sobra = []

for i in range(0, len(numeros) , 1):
    if (numeros[i] % 2 == 0):
        sobra.append(i)

print(sobra)

    