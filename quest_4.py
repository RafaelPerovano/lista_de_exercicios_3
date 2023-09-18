compras = ['pão', 'leite', 'carne']
cont = True
while cont:
    print('Sua lista: ', compras)
    parar = input('Se deseja adicionar mais itens digite enter, se não digite "parar".')
    if parar == 'parar':
        break

    itens = input('Digite os itens: ')

    compras.append(itens)

print('Sua lista ficou assim: ', compras)
