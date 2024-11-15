dinossario = {'a':1, 'b':2, 'c':3, 'd':4}

def items(dinossario):
    lista = []
    for itens in dinossario:
        tupla = (itens, dinossario[itens])
        lista += [tupla]

    return lista

def keys(dinossario):
    lista = []
    for chaves in dinossario:
        lista += [chaves]

    return lista

def values(dinossario):
    lista = []
    for valores in dinossario:
        lista += [dinossario[valores]]

    return lista

print(items(dinossario))
print(keys(dinossario))
print(values(dinossario))
