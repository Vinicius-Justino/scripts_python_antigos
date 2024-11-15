def lista_compra():
    lista = []
    def itens(item):
        nonlocal lista
        lista += [item]
        print(lista)
        
    return itens

a = lista_compra()

a('banana')
a('maçã')
a('carne')
a('cebola')
