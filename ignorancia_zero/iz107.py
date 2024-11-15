def get(dinossario, chave, valor=None):
    if chave in dinossario:
        return dinossario[chave]

    else:
        return valor

dinossario = {'a':1, 'b':2, 'c':3}

print(get(dinossario, 'a'))
print(get(dinossario, 'd'))
print(get(dinossario, 'd', 4))
