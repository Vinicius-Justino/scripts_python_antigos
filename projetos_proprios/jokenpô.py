from random import randint

def voceJoga():
    while True:
        jogada = input('\nDeseja jogar Pedra(0), Papel(1) ou Tesoura(2)? \n').lower()

        if jogada == '0' or jogada == '1' or jogada == '2':
            return int(jogada)
        else:
            print('escolha apenas entre as 3 opções.')

def computadorJoga():
    return randint(0, 2)

def mostraJogo(jogada, computador):
    if jogada == 0:
        saida1 = 'pedra.'
    elif jogada == 1:
        saida1 = 'papel.'
    elif jogada == 2:
        saida1 = 'tesoura.'

    if computador == 0:
        saida2 = 'pedra.'
    elif computador == 1:
        saida2 = 'papel.'
    elif computador == 2:
        saida2 = 'tesoura.'

    print('\nVocê jogou', saida1)
    print('Computador jogou', saida2)

def quemGanhou(jogada, computador):
    if jogada == computador:
        print('\nEmpate!')

    elif jogada == 0 and computador == 2:
        print('\nVocê ganhou!')
    elif jogada > computador:
        print('\nVocê ganhou!')

    elif computador == 2 and jogada == 0:
        print('\nVocê perdeu!')
    elif computador > jogada:
        print('\nVocê perdeu!')

def main():
    print('JOKENPÔ')
    jogando = True
    while jogando:
        jogada = voceJoga()
        computador = computadorJoga()
        mostraJogo(jogada, computador)
        quemGanhou(jogada, computador)

        while True:
            novamente = input('\nDeseja jogar novamente? \n').lower()

            if novamente[0] == 's':
                print('='*80)
                break
            elif novamente[0] == 'n':
                jogando = False
                break
            else:
                print('Digite apenas sim ou não.')

main()
