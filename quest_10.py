numeros = [200, 4, 3, 10, 5]
i = 0
while i < len(numeros):
    if numeros[i] %2 == 0:
        numeros[i] = 0
    i += 1
print(numeros)