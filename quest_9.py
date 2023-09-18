lista = ['pão', 'pé', 'carne', 200, 4, 3, 10, 5]
lista2 = ['mão', 'pé', 'carne', 100, 4, 2, 21, 5]
i = 0
c = 0
tem = False
itens = []
intens = []
while c < len(lista):
    while i < len(lista):
        if lista[c] == lista2[i]:
            intens = itens.append(lista[c])
            tem = True
        i += 1
    c += 1
    i = 0
if tem == False:
    print('Nao existe nenhum item que faz parte das duas listas. ')
else:
    print('Tem intem que faz parte das das listas. É/São: ', itens)