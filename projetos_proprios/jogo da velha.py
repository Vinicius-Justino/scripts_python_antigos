jogo = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
possiveis = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
jogadas = 0
jogador1 = 0
jogador2 = 0

def mostraJogo(jogo, jogadas):
    '''
Faz o jogo da velha aparecer assim na tela:

         1   2   3
         |   |   |

           |   |   
    A-   X | O |
        ___|___|___
           |   |
    B-   O | X | O  
        ___|___|___
           |   |
    C-     |   | X
           |   |
    '''
    linha1 = '\tA-   ' + jogo[0][0] + ' | ' + jogo[0][1] + ' | ' + jogo[0][2] + ' '
    linha2 = '\tB-   ' + jogo[1][0] + ' | ' + jogo[1][1] + ' | ' + jogo[1][2] + ' '
    linha3 = '\tC-   ' + jogo[2][0] + ' | ' + jogo[2][1] + ' | ' + jogo[2][2] + ' '

    if jogadas%2 != 0:
        print('\nJogador 1')
    elif jogadas%2 == 0:
        print('\nJogador 2')

    print('\t     1   2   3 ')
    print('\t     |   |   | ')
    print('\t               ')
    print('\t       |   |   ')
    print(linha1)
    print('\t    ___|___|___')
    print('\t       |   |   ')
    print(linha2)
    print('\t    ___|___|___')
    print('\t       |   |   ')
    print(linha3)
    print('\t       |   |   ')

def recebeJogada(jogo, possiveis, jogadas):
    '''
Verifica se as posições para a jogada são possíveis, executando-as se sim
    '''
    while True:
        jogada = input('\nDigite a posição em que deseja jogar: ')

        if jogada in possiveis:
            possiveis.remove(jogada)
            break
        else:
            print('Essa posição já deve estar ocupada ou não existe, tente novamente.')

    if jogada[0] == 'a':
        linha = 0
    elif jogada[0] == 'b':
        linha = 1
    elif jogada[0] == 'c':
        linha = 2

    posiçao = int(jogada[1]) - 1

    if jogadas%2 != 0:
        jogo[linha][posiçao] = 'X'
    elif jogadas%2 == 0:
        jogo[linha][posiçao] = 'O'

def verificaJogo(jogo, jogando):
    '''
Verifica se o jogo terminou
    '''
    if jogo[0][0] == jogo[0][1] == jogo[0][2] and jogo[0][0] != ' ':
        jogando = False
    elif jogo[1][0] == jogo[1][1] == jogo[1][2] and jogo[1][1] != ' ':
        jogando = False
    elif jogo[2][0] == jogo[2][1] == jogo[2][2] and jogo[2][2] != ' ':
        jogando = False
    elif jogo[0][0] == jogo[1][0] == jogo[2][0] and jogo[0][0] != ' ':
        jogando = False
    elif jogo[0][1] == jogo[1][1] == jogo[2][1] and jogo[1][1] != ' ':
        jogando = False
    elif jogo[0][2] == jogo[1][2] == jogo[2][2] and jogo[2][2] != ' ':
        jogando = False
    elif jogo[0][0] == jogo[1][1] == jogo[2][2] and jogo[0][0] != ' ':
        jogando = False
    elif jogo[0][2] == jogo[1][1] == jogo[2][0] and jogo[1][1] != ' ':
        jogando = False
    elif jogo[0].count(' ') == 0 and jogo[1].count(' ') == 0 and jogo[2].count(' ') == 0:
        jogando = False
    else:
        jogando = True

    return jogando

def main():
    '''
Função principal do programa
    '''
    global jogo, possiveis, jogadas, jogador1, jogador2
    jogando = True
    partida = True

    print('JOGO DA VELHA')
    while jogando:
        jogo = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        possiveis = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
        jogadas = 0
        partida = True
        while partida:
            jogadas += 1
            mostraJogo(jogo, jogadas)
            recebeJogada(jogo, possiveis, jogadas)
            partida = verificaJogo(jogo, partida)

        mostraJogo(jogo, jogadas)
        
        if jogo[0].count(' ') == 0 and jogo[1].count(' ') == 0 and jogo[2].count(' ') == 0:
            print('\nVelha!')
        elif jogadas%2 != 0:
            print('\nJogador 1 ganhou!')
            jogador1 += 1
        elif jogadas%2 == 0:
            print('\nJogador 2 ganhou!')
            jogador2 += 1

        print('\nPlacar:')
        print('\nJogador 1: {} pontos'.format(jogador1))
        print('Jogador 2: {} pontos'.format(jogador2))

        while True:
            continuar = input('\nDeseja jogar novamente? \n').lower()

            if continuar[0] == 's':
                jogando = True
                break
            elif continuar[0] == 'n':
                jogando = False
                break
            else:
                print('Não entendo como uma resposta, digite apenas sim ou não.')

main()
            
