numeros = [200, 4, 3, 10, 5]
numero_maior = numeros[0]
numero_menor = numeros[0]
i = 1
while i < len(numeros):
    if numeros[i] > numero_maior:
        numero_maior = numeros[i]
    if numeros[i] < numero_menor:
        numero_menor = numeros[i]
    i += 1
print('Seu numero menor é {} e seu numero maior é {}'.format(numero_menor, numero_maior))