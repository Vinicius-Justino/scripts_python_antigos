def remove(numero, arg_lista):
    global lista
    '''
remove todos os número na lista escolhida iguais ao digitado pelo usuário.
    '''
    aux = []
    for remoçao in range(len(lista)):
        if lista[remoçao] == numero:
            continue

        aux += [lista[remoçao]]

    lista = aux

    return lista

lista = []

for teste in range(10):
    n = int(input('você já sabe o que fazer: '))

    lista += [n]

remove(3, lista)
print(lista)
