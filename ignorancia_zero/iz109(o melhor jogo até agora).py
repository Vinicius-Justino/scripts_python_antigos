#FALTA:
# - ARRUMAR OS BUGS DO JOGO
# - TALVEZ IMPLEMENTAR UM SISTEMA DE RECORDES

from random import *

#COISAS IMPORTANTES
inimigos = [[('ogro',), [30, 5, 100, 5], ['Clavada']], [('goblin',), [15, 10, 70, 10], ['Flechada']], [('esqueleto',), [20, 20, 80, 20], ['Espadada', 'Cura']], [('bruxo',), [10, 30, 80, 20], ['Relâmpago', 'Bola de Fogo', 'Espadada', 'Cura']]]
jogador = ([None], [20, 20, 500, 100])
inimigos_mortos = 0
n_inimigos = 1
tropa = []
vitorias = 0

#ESCOLHE INIMIGOS
def escolheInimigos(n_inimigos, l_inimigos):       # FUNCIONA
    '''
Monta uma tropa para lutar contra o jogador
    '''
    tropa = []
    
    for escolhe in range(n_inimigos):
        inimigo = choice(l_inimigos)
        tropa += [inimigo.copy()]

    return tropa

#RECEBE AÇÃO 1
def recebeAçao1():    # TEM QUE TESTAR
    '''
Recebe um comando do jogador e verifica se é válido.
    '''
    while True:
        açao = input('\nDeseja começar um novo jogo(n), carregar um jogo(c), ou sair(s)? \n').lower()
        
        if açao[0] != 'n' and açao[0] != 'c' and açao[0] != 's': 
            print('Por favor, escolha apenas entre as 3 opções abaixo.')
        else:
            return açao[0]

#RECEBE AÇÃO 2
def recebeAçao2():   # TEM QUE TESTAR
    '''
Recebe um comando do jogador e verifica se é válido.
    '''
    while True:
        açao = input('\nDeseja salvar(s), lutar(l) ou abandonar o jogo(a)? \n').lower()

        if açao[0] != 's' and açao[0] != 'l' and açao[0] != 'a':
            print('Por favor, escolha apenas entre as 3 opções abaixo.')
        else:
            return açao[0]

#RECEBE AÇÃO 3
def recebeAçao3():    # TEM QUE TESTAR
    '''
Recebe um comando de ataque do jogador e verefica se é válido.
    '''
    print('\nHP: {}'.format(jogador[1][2]))
    print('SP: {}'.format(jogador[1][3]))
    while True:
        açao = input('\nDeseja usar Lança de Gelo, Espadada, Flexada ou Cura? \n').upper()

        if açao[0] == 'L' or açao[0] == 'C':
            if jogador[1][3]-10 < 0:
                print('SP insuficiente para efeturar essa ação.')
            else:
                if açao[0] == 'L':
                    açao = 'Lança de Gelo'
                elif açao[0] == 'C':
                    açao = 'Cura'
                    
                jogador[1][3] -= 10
                return açao

        elif açao[0] == 'F':
            if jogador[1][3]-2 < 0:
                print('SP insuficiente para efeturar essa ação.')
            else:
                açao = 'Flechada'
                jogador[1][3] -= 2
                return açao

        elif açao[0] == 'E':
            açao = 'Espadada'
            return açao

        else:
            print('Por favor, escolha apenas entre as 4 opções abaixo.')

#APRIMORA O JOGADOR
def aprimoraJogador(jogador):      # TEM QUE TESTAR
    '''
Recebe um comando de up-grade dos status do do jogador e verifica se é válido
    '''
    while True:
        açao = input('\nDeseja aprimorar seus atributos(1) ou recuperar sua vida e SP(2)? \n')

        if açao != '1' and açao != '2':
            print('Por favor, escolha apenas entra as 2 opções abaixo.')
        else:
            break

    if açao == '1':
        while True:
            melhora = input('Deseja aumentar ataque ou defesa? \n').lower()

            if melhora[0] == 'a':
                jogador[1][0] += 5
                print('Seu ataque agora é {}!'.format(jogador[1][0]))
                break

            if melhora[0] == 'd':
                jogador[1][1] += 5
                print('Sua defesa agora é {}!'.format(jogador[1][1]))
                break
                
            else:
               print('Por favor, escolha apenas entre ataque e defesa.')

    elif açao == '2':
        jogador[1][2] = 500
        jogador[1][3] = 100
        print('Você foi restaurado!')

    return jogador

#CALCULA DANO
def calculaDano(ataque, força, defesa):  #TEM QUE TESTAR
    '''
Calcula o dano causado em combate.
    '''
    if ataque[0] == 'E' or ataque[0] == 'C':
        dano = max(round((força - defesa/1)*random()), 1)
    elif ataque[0] == 'F':
        dano = max(round((força - defesa/3)*random()), 1)
    else:
        dano = max(round((força - defesa/5)*random()), 1)

    return dano

#TURNO DO JOGADOR
def turnoJogador(açao, tropa, n_inimigos, jogador):       # TEM QUE TESTAR
    '''
Executa as ações do jogador.
    '''
    if açao != 'Cura':
        cont_aux = 1
        print('\nEscolha um alvo:')
        for mostra in tropa:
            if mostra[1][2] >= 1:
                saida = str(cont_aux) + ' '*(len(str(n_inimigos))-len(str(cont_aux))) + ' - '
            else:
                saida = 'X' + ' '*(len(str(n_inimigos)) - 1) + ' - '
                
            saida += mostra[0][0] + ' '*(10-len(mostra[0][0])) + ' - '

            if mostra[1][2] >= 1:
                saida += 'HP ' + str(mostra[1][2]) + ' '*(3-len(str(mostra[1][2])))
                saida += ' / SP ' + ' '*(2-len(str(mostra[1][3]))) + str(mostra[1][3])
            else:
                saida += 'Morto'
                
            print(saida)
            cont_aux += 1

        while True:
            alvo = input('\nQuem vai atacar: ')

            erro = False
            numero = True

            for confere in alvo:
                if not '0' <= confere <= '9':
                    print('Digite o número do inimigo que quer atacar.')
                    erro = True
                    numero = False
                    break

            if numero:
                if int(alvo) <= 0 or int(alvo) > n_inimigos:
                    print('Digite apenas o número que precede o nome do inimigo que quer atacar.')
                    erro = True

            if erro != True and tropa[int(alvo)-1][1][2] < 1:
                print('Escolha apenas entre os inimigos vivos.')
                erro = True
                
            if erro == False:
                alvo = int(alvo)-1
                break

        dano = calculaDano(açao, jogador[1][0], tropa[alvo][1][1])
        tropa[alvo][1][2] -= dano

        print('Usou {} e deu {} de dano ao {}!'.format(açao, dano, tropa[alvo][0][0]))

        if tropa[alvo][1][2] < 1:
            print('{} morreu!'.format(tropa[alvo][0][0]))

    elif açao == 'Cura':
        if jogador[1][2]+10 <= 500:
            jogador[1][2] += 10
        else:
            jogador[1][2] = 500

        print('Curou 10 de vida!')

    return tropa, jogador

#TURNO DO INIMIGO
def turnoInimigo(tropa, jogador):   # TEM QUE TESTAR
    '''
Sorteia os ataques do inimigos e garante que eles podem ser usados.
    '''
    print('')
    for inimigo in tropa:
        if inimigo[1][2] >= 1:
            while True:
                ataque = choice(inimigo[2])

                if ataque == 'Bola de Fogo' or ataque == 'Cura':
                    if inimigo[1][3]-10 >= 0:
                        inimigo[1][3] -= 10
                        break

                elif ataque == 'Relâmpago':
                    if inimigo[1][3]-5 >= 0:
                        inimigo[1][3] -= 5
                        break

                elif ataque == 'Flechada':
                    if inimigo[1][3]-2 >= 0:
                        inimigo[1][3] -= 2
                        break

                elif ataque == 'Espadada' or ataque == 'Clavada':
                    break

            if ataque != 'Cura':
                dano = calculaDano(ataque, inimigo[1][0], jogador[1][1])
                jogador[1][2] -= dano
                print('{} usou {} e te deu {} de dano!'.format(inimigo[0][0], ataque, dano))

            elif ataque == 'Cura':
                if inimigo[1][2] + 10 <= 80:
                    inimigo[1][2] += 10
                else:
                    inimigo[1][2] =  80
                    
                print('{} curou 10 de vida!'.format(inimigo[0][0]))

    return tropa, jogador

#SALVAR O JOGO
def salvaJogo(vitorias, jogador, n_inimigos, inimigos_mortos):     #TEM QUE TESTAR
    '''
cria um documento que guarda as informações do jogador para continuar jogando depois
    '''
    save_slot = open('Save Slot(melhor jogo até agora).txt', 'w')

    save_slot.write('{} \n'.format(vitorias))
    save_slot.write('{} \n'.format(jogador))
    save_slot.write('{} \n'.format(n_inimigos))
    save_slot.write('{}'.format(inimigos_mortos))

    save_slot.close()
        
#VERIFICA
def verificaJogo(jogador, tropa):       #TEM QUE TESTAR
    '''
Verifica se o jogo acabou e qual foi o resultado da partida
    '''
    todos = len(tropa)
    mortos = 0
    for contagem in tropa:
        if contagem[1][2] < 1:
            mortos += 1

    if mortos == todos:
        final = 'ganhou'
    elif jogador[1][2] < 1:
        final = 'perdeu'
    else:
        final = 'continua'

    return final

def main():
    '''
Função principal do programa.
    '''
    global jogador, vitorias, inimigos, n_inimigos, inimigos_mortos, tropa

    while True:
        açao = recebeAçao1()

        if açao == 'c':
            save_slot = open('Save Slot(melhor jogo até agora).txt')

            vitorias = eval(save_slot.readline())
            jogador = eval(save_slot.readline())
            n_inimigos = eval(save_slot.readline())
            inimigos_mortos = eval(save_slot.readline())

        elif açao == 'n':
            nome = input('\nDigite o seu nome: ')
            jogador[0][0] = nome

            print('\nBom {}, o jogo é simples:'.format(nome))
            print('\n- A cada rodada você pode escolher entre salvar o jogo, entrar em combate ou sair')
            print('- Uma que você entra em combate, terá de enfrentar todos os inimigos')
            print('- Se sua vida chegar em 0, fim de jogo')
            print('- Se sobreviver, poderá escolher entre aumentar os seus tributos ou se curar')
            print('- A cada 10 inimigos vencidos o número de inimigos para enfrentar dobrar')
            print('\nBoa sorte!')

        elif açao == 's':
            break

        while True:
            açao = recebeAçao2()
            tropa = escolheInimigos(n_inimigos, inimigos)

            if açao == 's':
                salvaJogo(vitorias, jogador, n_inimigos, inimigos_mortos)

            elif açao == 'l':
                while True:
                    açao = recebeAçao3()
                    turnoJogador(açao, tropa, n_inimigos, jogador)
                    turnoInimigo(tropa, jogador)
                    final = verificaJogo(jogador, tropa)

                    if final == 'ganhou':
                        print('\nParabéns, {}! você concluiu o desafio.'.format(jogador[0][0]))
                        aprimoraJogador(jogador)
                        vitorias += 1
                        inimigos_mortos += n_inimigos
                        if inimigos_mortos >= 10:
                            n_inimigos *= 2
                            inimigos_mortos = 0
                        break

                    elif final == 'perdeu':
                        print('\nInfelizmente você perdeu.')
                        vitorias = 0
                        inimigos_mortos = 0
                        n_inimigos = 1
                        jogador[1][0] = 20
                        jogador[1][1] = 20
                        break

            elif açao == 'a':
                break

main()
