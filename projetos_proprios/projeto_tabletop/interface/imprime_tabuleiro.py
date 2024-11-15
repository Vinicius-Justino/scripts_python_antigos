'''
         1   2   3
        ___________
       |   |   |   |   1
       |   |   |   |   2    1
       |___|___|___|   3 
       |   |   |   |   4
       |   |   |   |   5    2
       |___|___|___|   6
       |   |   |   |   7
       |   |   |   |   8    3
       |___|___|___|   9    
       |   |   |   |  10    
       |   |   |   |  11    4
       |___|___|___|  12
       |   |   |   |  13
       |   |   |   |  14    5
       |___|___|___|  15
       |   |   |   |  16
       |   |   |   |  17    6
       |___|___|___|  18
       |   |   |   |  19
       |   |   |   |  20    7
       |___|___|___|  21
       |   |   |   |  22
       |   |   |   |  23    8
       |___|___|___|  24
       |   |   |   |  25
       |   |   |   |  26    9
       |___|___|___|  27
       |   |   |   |  28
       |   |   |   |  29   10
       |___|___|___|  30
'''
# PARA TERMINAR
# - TESTAR ESSA FUNÇÃO E ARRUMAR POSSÍVEIS PROBLEMAS

def ImprimeTabuleiro(posiçoes, jogador):
    print('\n {} \n'.format(jogador.nome))
    print('    ', end='')

    for indica in range(1, 13):
        if indica == 1:
            print('   {}'.format(indica), end='')
        elif indica != 12 and indica < 10:
            print('    {}'.format(indica), end='')
        elif indica != 12 and indica >= 10:
            print('   {}'.format(indica), end='')
        else:
            print('   {}'.format(indica))

    print('    ', '_'*59)
    quadrados = 0
    for linhas in range(1, 37):
        if linhas - quadrados*3 == 1:
            saida = '    |'
            saida += '    |'*12
            
        elif linhas - quadrados*3 == 2:
            saida = ' '+ chr(quadrados+97) + '  | '
            for completa in range(12):
                try:
                    saida += posiçoes[quadrados][completa].dono + posiçoes[quadrados][completa].tipo + ' | '
                except:
                    saida += posiçoes[quadrados][completa] + '  | '

            quadrados += 1

        elif linhas - quadrados*3 == 0:
            saida = '    |'
            saida += '____|'*12

        if linhas == 9:
            saida += ' <== Jogador 1'

        if linhas == 18:
            saida += '_'*14

        if linhas == 27:
            saida += ' <== Jogador 2'
        print(saida)

if __name__ == '__main__':
    posiçoes = [[], [], [], [], [], [], [], [], [], [], [], []]
    for preenche1 in range(12):
        for preenche2 in range(12):
            posiçoes[preenche1] += ' '*2

    class teste(object):
        def __init__(self, dono, tipo):
            self.dono = dono
            self.tipo = tipo
        def __str__(self):
            return 'Dono: {} \nTipo: {}'.format(self.dono, self.tipo)

    class jogadorr(object):
        def __init__(self, nome):
            self.nome = nome

    jogador1 = jogadorr('Vini')
    mago = teste('☺', '♥')
    elfo = teste('☻', '♣')
    soldado1 = teste('☺', '♠')
    soldado2 = teste('☻', '♠')
    dragao1 = teste('☺', '♦')
    dragao2 = teste('☻', '♦')
    
             
    posiçoes[6][8] = mago
    posiçoes[8][1] = mago
    posiçoes[7][4] = mago
    posiçoes[9][11] = mago
    posiçoes[10][2] = soldado1
    posiçoes[2][6] = elfo
    posiçoes[1][9] = elfo
    posiçoes[4][10] = elfo
    posiçoes[2][5] = soldado2
    posiçoes[3][7] = soldado2
    posiçoes[0][4] = dragao1
    posiçoes[0][5] = dragao1
    posiçoes[0][6] = dragao1
    posiçoes[0][7] = dragao1
    posiçoes[0][8] = dragao1
    posiçoes[0][9] = dragao1
    posiçoes[11][4] = dragao2
    posiçoes[11][5] = dragao2
    posiçoes[11][6] = dragao2
    posiçoes[11][7] = dragao2
    posiçoes[11][8] = dragao2
    posiçoes[11][9] = dragao2
    
    ImprimeTabuleiro(posiçoes, jogador1)

    input('\nDigite para sair: ')
