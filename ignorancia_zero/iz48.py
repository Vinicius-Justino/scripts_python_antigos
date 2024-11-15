cont = 0
aux = 0
lista = []
vetor = 0
while vetor != -1:
    vetor = int(input('digite o número {}: '.format(aux+1)))
    lista += [vetor]
    aux += 1

elemento = int(input('digite o número que quer procurar: '))

while aux >= 0:
    if lista[aux-1] == elemento:
        cont += 1

    aux -= 1

print('existem {} números {} na sequência digitada.'.format(cont, elemento))
