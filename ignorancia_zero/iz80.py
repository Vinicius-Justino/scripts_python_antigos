def tabuada():
    cont = 0
    def contas(x):
        nonlocal cont
        cont += 1
        for numeros in range(1, 11):
            print('{} * {} = {}'.format(cont, numeros, cont*numeros))
        print('')

        if cont != x:
            contas(x)

    return contas

a = tabuada()

a(100)
