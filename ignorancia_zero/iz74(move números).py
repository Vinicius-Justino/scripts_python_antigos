from random import choice

matriz = []
matriz_correta = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,'*']]
vazio = [0, 0]
linha = 0
coluna = 0

def main():
    criaJogo()
    jogada()

def criaJogo():
    while True:
        global vazio, matriz
        matriz = []
        numeros = list(range(15))
        numeros += ['*']
        for linhas in range(4):
            linha = []
            for colunas in range(4):
                n = choice(numeros)
                numeros.remove(n)
                linha += [n]

            matriz += [linha]

        if matriz != matriz_correta:
            for vazio1 in range(4):
                print(matriz)
                for vazio2 in range(4):
                    if matriz[vazio1][vazio2] == '*':
                        vazio[0] = matriz[vazio1]
                        vazio[1] = matriz[vazio2]
                        break
            break

def jogada():
    global linha, coluna, matriz
    for jogo in range(4):
        print(matriz[jogo])
    print('')
    
    linha = int(input('digite a linha do número que deseja mover: '))
    coluna = int(input('digite a coluna do número que deseja mover: '))

    posiçao = [linha-1, coluna-1]
    aux = []

    if posiçao[0] == vazio[0]:
        if posiçao[1] == vazio[1]+1 or posiçao[1] == vazio[1]-1:

            matriz[vazio[0]][vazio[1]] = matriz[linha][coluna]
            matriz[linha][coluna] = matriz[vazio[0]][vazio[1]]

            vazio[0] = linha
            vazio[1] = coluna


main()

