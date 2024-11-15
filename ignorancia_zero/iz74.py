def fazer_matriz(linhas, colunas):
    global matriz
    for loop1 in range(linhas):
        linha = []
        for elementos in range(colunas):
            num = int(input('digite o elemento {}-{}: '.format(loop1+1, elementos+1)))
            linha += [num]

        matriz += [linha]

    print('')

    for prints in range(len(matriz)):
        print(matriz[prints])

    print('')

def reorganizar():
    global matriz
    troca1 = []
    troca1 += [int(input('digite a linha do 1º número: '))]
    troca1 += [int(input('digite a coluna do 1º número: '))]

    print('')
    
    troca2 = []
    troca2 += [int(input('digite a linha do 2º número: '))]
    troca2 += [int(input('digite a coluna do 2º número: '))]

    n1 = matriz[troca1[0]-1][troca1[1]-1]
    n2 = matriz[troca2[0]-1][troca2[1]-1]

    matriz[troca1[0]-1][troca1[1]-1] = n2
    matriz[troca2[0]-1][troca2[1]-1] = n1

    print('')
    
    for prints in range(len(matriz)):
        print(matriz[prints])    

linhas = int(input('digite o número de linhas na matriz: '))
colunas = int(input('digite o número de colunas na matriz: '))

print('')

matriz = []
fazer_matriz(linhas, colunas)
reorganizar()
