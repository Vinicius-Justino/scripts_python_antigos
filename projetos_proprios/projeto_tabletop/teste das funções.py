from peças.classes import *
from peças.administra_peças import *
from interface.administra_jogadas import *
from interface.imprime_tabuleiro import *
from random import choice

#PARA TERMINAR
# - IMPORTAR TODAS AS OUTRAS COISAS E FAZER ELAS FUNCIONAR EM UM JOGO.
# - ARRUMAR OS ITENS.
# - TESTAR TUDO E ARRUMAR.

jogador1 = jogador('Jogador 1', '☺', 1)
urna1 = CriaUrna(jogador1)
dragao1_1 = dragao(jogador1)
dragao1_2 = dragao1_1
dragao1_3 = dragao1_1
dragao1_4 = dragao1_1
dragao1_5 = dragao1_1
dragao1_6 = dragao1_1
jogador1.urna = urna1
jogador1.dragao = dragao1_1

jogador2 = jogador('Jogador 2', '☻', 10)
urna2 = CriaUrna(jogador2)
dragao2_1 = dragao(jogador2)
dragao2_2 = dragao2_1
dragao2_3 = dragao2_1
dragao2_4 = dragao2_1
dragao2_5 = dragao2_1
dragao2_6 = dragao2_1
jogador2.urna = urna2
jogador2.dragao = dragao2_1

tabuleiro = [[], [], [], [], [], [], [], [], [], [], [], [], [], []]
for preenche1 in range(12):
    for preenche2 in range(12):
        tabuleiro[preenche1] += ' '

tabuleiro[0][3] = dragao1_1
tabuleiro[0][4] = dragao1_2
tabuleiro[0][5] = dragao1_3
tabuleiro[0][6] = dragao1_4
tabuleiro[0][7] = dragao1_5
tabuleiro[0][8] = dragao1_6
tabuleiro[11][3] = dragao2_1
tabuleiro[11][4] = dragao2_2
tabuleiro[11][5] = dragao2_3
tabuleiro[11][6] = dragao2_4
tabuleiro[11][7] = dragao2_5
tabuleiro[11][8] = dragao2_6

jogadas = 1

for teste in range(15):
    if jogadas%2 != 0:
        jogador_atual = jogador1
    elif jogadas%2 == 0:
        jogador_atual = jogador2

    moviveis = MovimentosPossiveis(jogador_atual, tabuleiro)
    
    ImprimeTabuleiro(tabuleiro, jogador_atual)

    peça = None

    while peça == None:
        peça = ConvertePeça(SacaPeça(jogador_atual.urna, jogador_atual, tabuleiro), jogador_atual)
    
    try:
        print('\nVocê sacou a peça "{}".'.format(peça.nome))
    except:
        print('\nVocê sacou a peça "{}".'.format(peça.classe))
    RecebeJogada(jogador_atual, peça, tabuleiro)
    
    #Move Peças
    for move in range(2):
        if moviveis != []:
            ImprimeTabuleiro(tabuleiro, jogador_atual)
            MovePeças(jogador_atual, tabuleiro, moviveis)

    #Ataca
    usaveis = AtaquesPossiveis(jogador_atual, tabuleiro)
    while usaveis != []:
        print(usaveis)
        ImprimeTabuleiro(tabuleiro, jogador_atual)
        while True:
            vai_atacar = input('\nDeseja atacar? \n').lower()

            if vai_atacar[0] == 's':
                break
            elif vai_atacar[0] == 'n':
                break
            else:
                print('Por favor, escolha apenas entre sim ou não.')

        if vai_atacar[0] == 's':
            FazAtaques(jogador_atual, tabuleiro, usaveis)
        elif vai_atacar[0] == 'n':
            break
        
    jogadas += 1
