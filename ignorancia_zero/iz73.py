def fazer_matriz(linhas, colunas):
    matriz = []
    for loop1 in range(linhas):
        linha = []
        for elementos in range(colunas):
            num = int(input('digite o elemento {}-{}: '.format(loop1, elementos)))
            linha += [num]

        matriz += [linha]

    for prints in range(len(matriz)):
        print(matriz[prints])

linhas = int(input('digite o número de linhas na matriz: '))
colunas = int(input('digite o número de colunas na matriz: '))

print('')

fazer_matriz(linhas, colunas)
