cont = True
parar = 0
words = []

while cont:
    palavras = input('Digite alguma palavra: ')
    
    if len(palavras) > 5:
        words.append(palavras)

    parar = str(input(('se quiser parar digite 1, se n de enter. ')))
    if parar == '1':
        break
    
print(words)
