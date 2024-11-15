from random import choice

matriz = []
matriz_correta = [[0,1,2,3], [4,5,6,7], [8,9,10,11], [12,13,14,' ']]
vazio = [0, 0]
linha = 0
coluna = 0

def criaJogo():
    while True:
        global vazio, matriz
        matriz = []
        numeros = list(range(15))
        numeros += [' ']
        for linhas in range(4):
            linha = []
            for colunas in range(4):
                n = choice(numeros)
                numeros.remove(n)
                linha += [n]

            matriz += [linha]

        if matriz != matriz_correta:
            for vazio1 in range(4):
                for vazio2 in range(4):
                    if matriz[vazio1][vazio2] == ' ':
                        vazio[0] = [vazio1]
                        vazio[1] = [vazio2]
                        break
            break
def mostraJogo(x):
    for jogo in range(4):
        for formata in range(4):
            saida = str(x[jogo][formata]) + ' '*(2-len(str(x[jogo][formata])))
            print(saida, end=' ')
        print('\n')
    
def jogada():
    global linha, coluna, matriz

    while True:
        linha = input('digite a linha do número que deseja mover: ')
        coluna = input('digite a coluna do número que deseja mover: ')

        if '1' <= linha <= '4' and '1' <= coluna <= '4':
            linha = int(linha)
            coluna = int(coluna)
            break

        else:
            print('digite apenas números entre 1 e 4.')
            print('')

    posiçao = [[linha-1], [coluna-1]]

    if posiçao[0] == vazio[0]:
        if posiçao[1][0] == vazio[1][0]+1 or posiçao[1][0] == vazio[1][0]-1:
            aux1 = matriz[vazio[0][0]][vazio[1][0]]
            aux2 = matriz[posiçao[0][0]][posiçao[1][0]]
            
            matriz[vazio[0][0]][vazio[1][0]] = aux2
            matriz[posiçao[0][0]][posiçao[1][0]] = aux1

            vazio[0][0] = linha - 1
            vazio[1][0] = coluna - 1

        else:
            print("não é uma jogada válida, mova apenas números adjascentes ao espaço vazio.")
            print('')

    elif posiçao[1] == vazio[1]:
        if posiçao[0][0] == vazio[0][0]+1 or posiçao[0][0] == vazio[0][0]-1:
            aux1 = matriz[vazio[0][0]][vazio[1][0]]
            aux2 = matriz[posiçao[0][0]][posiçao[1][0]]
            
            matriz[vazio[0][0]][vazio[1][0]] = aux2
            matriz[posiçao[0][0]][posiçao[1][0]] = aux1

            vazio[0][0] = linha - 1
            vazio[1][0] = coluna - 1

        else:
            print("não é uma jogada válida, mova apenas números adjascentes ao espaço vazio.")
            print('')

    else:
        print("não é uma jogada válida, mova apenas números adjascentes ao espaço vazio.")
        print('')

    mostraJogo(matriz)

def main():
    criaJogo()
    print('deixe seu tabuleiro assim:')
    print('')
    mostraJogo(matriz_correta)
    print("para fazer isso, troque o espaço vazio de lugar com os números adjascentes:")
    print('')
    print("      1                  ")
    print("    2   3  --->  2 1 3   ")
    print("      4            4     ")
    print('ou:')
    print("      1            1     ")
    print("    2   3  --->    2 3   ")
    print("      4            4     ")
    print('')
    mostraJogo(matriz)
    while True:
        jogada()

        if matriz == matriz_correta:
            print('parabéns, você ganhou!')
            break

main()

