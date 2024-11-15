# PARA TERMINAR
# - TESTAR A FUNÇÃO DE FAZER JOGADAS.
# - ARRUMAR A FUNÇAO DE ATACAR COM AS PEÇAS.
# - ARRUMAR O MAIOR NÚMERO DE PROBLEMAS.

from random import choice

##=================================================== RECEBE AS JOGADAS ===================================================##
def RecebeJogada(jogador, peça, tabuleiro):
    if peça.classe == 'Arma':
        while True:
            try:
                jogada = input('\nDigite a posição da peça que deseja equipar: ').lower()

                if not 'a' <= jogada[0] <= 'l':
                    print('Por favor, escolha apenas as linhas entre A e L.')
                elif not 1 <= int(jogada[1:]) <= 12:
                    print('Por favor, digite apenas a coluna correspondente à coluna da peça.')
                elif tabuleiro[ord(jogada[0])-97][int(jogada[1:])-1] == ' ':
                    print('Não há nenhuma peça nessa posição, digite novamente.')
                elif jogador.marca != tabuleiro[ord(jogada[0])-97][int(jogada[1:])-1].dono:
                    print('Essa peça não é sua. ', end='')
                    print(jogador)
                elif tabuleiro[ord(jogada[0])-97][int(jogada[1:])-1].tipo not in peça.tipos:
                    print('Essa peça não é compatível. ', end='')
                    print(peça)
                elif tabuleiro[ord(jogada[0])-97][int(jogada[1:])-1].arma.nome == peça.nome:
                    print('Você já equipou essa peça.')
                else:
                    tabuleiro[ord(jogada[0])-97][int(jogada[1:])-1].arma = peça
                    peça.Efeito(tabuleiro[ord(jogada[0])-97][int(jogada[1:])-1])
                    print('O {} em {} foi equipado com {}! O ataque dele agora é {}.'.format(tabuleiro[ord(jogada[0])-97][int(jogada[1:])-1].classe, chr(tabuleiro[ord(jogada[0])-97][int(jogada[1:])-1].posiçao[0][0]+97)+str(tabuleiro[ord(jogada[0])-97][int(jogada[1:])-1].posiçao[1][0]+1), peça.nome, tabuleiro[ord(jogada[0])-97][int(jogada[1:])-1].ataque))
                    break
            except:
                print('Houve um problema na hora de analisar o seu comando, tente novamente.')
                             
    elif peça.classe == 'Item' or peça.classe == 'Poção':
        while True:
            try:
                jogada = input('\nDigite a posição da peça que deseja entregar o item: ').lower()

                if not 'a' <= jogada[0] <= 'l':
                    print('Por favor, escolha apenas as linhas entre A e L.')
                elif not 1 <= int(jogada[1:]) <= 12:
                    print('Digite apenas o número correspondente à coluna da peça.')
                elif tabuleiro[ord(jogada[0])-97][int(jogada[1:])-1] == ' ':
                    print('Não há nenhuma peça nessa posição.')
                elif jogador.marca != tabuleiro[ord(jogada[0])-97][int(jogada[1:])-1].dono:
                    print('Essa peça não é sua.', end=' ')
                    print(jogador)
                elif tabuleiro[ord(jogada[0])-97][int(jogada[1:])-1].tipo not in peça.tipos:
                    print('Essa peça não é compatível. ')
                    print(peça)
                else:
                    if peça.classe == 'Item':
                        try:
                            if tabuleiro[ord(jogada[0])-97][int(jogada[1:])-1].item.nome != peça.nome:
                                tabuleiro[ord(jogada[0])-97][int(jogada[1:])-1].item = peça
                                peça.Efeito(tabuleiro[ord(jogada[0])-97][int(jogada[1:])-1])
                                print('{} em {} foi equipado com {}!'.format(tabuleiro[ord(jogada[0])-97][int(jogada[1:])-1].classe, chr(tabuleiro[ord(jogada[0])-97][int(jogada[1:])-1].posiçao[0][0]+97)+str(tabuleiro[ord(jogada[0])-97][int(jogada[1:])-1].posiçao[1][0]+1), peça.nome))
                                break
                            else:
                                print('Essa peça já tem esse item.')
                        except:
                            tabuleiro[ord(jogada[0])-97][int(jogada[1:])-1].item = peça
                            peça.Efeito(tabuleiro[ord(jogada[0])-97][int(jogada[1:])-1])
                            break
                        
                    elif peça.classe == 'Poção':
                        if tabuleiro[ord(jogada[0])-97][int(jogada[1:])-1].poçao == False:
                            peça.Efeito(tabuleiro[ord(jogada[0])-97][int(jogada[1:])-1])
                            tabuleiro[ord(jogada[0])-97][int(jogada[1:])-1].poçao = True
                            print('Você curou o {} em {}! agora ele está com {} de vida.'.format(tabuleiro[ord(jogada[0])-97][int(jogada[1:])-1].classe, chr(tabuleiro[ord(jogada[0])-97][int(jogada[1:])-1].posiçao[0][0]+97)+str(tabuleiro[ord(jogada[0])-97][int(jogada[1:])-1].posiçao[1][0]+1), tabuleiro[ord(jogada[0])-97][int(jogada[1:])-1].vida))
                            break
                        else:
                            print('Você já usou essa poção nessa peça.')                
            except:
                print('Houve um problema na hora de analisar o seu comando, tente novamente.')

    else:
        while True:
            try:
                jogada = int(input('\nDigite a coluna em que deseja colocar a peça: '))

                try:
                    if tabuleiro[jogador.começo][jogada-1].posiçao[0][0] == jogador.começo and tabuleiro[jogador.começo][jogada-1].posiçao[1][0] == jogada-1:
                        print('Esta posição está ocupada, tente novamente')
                except:
                    if 1 <= jogada <= 12:
                        tabuleiro[jogador.começo][jogada-1] = peça
                        peça.posiçao[0] = [jogador.começo]
                        peça.posiçao[1] = [jogada-1]
                        break
                    else:
                        print('Por, favor, digite apenas número entre 1 e 12.')
            except:
                print('Houve um erro ao analisar o seu comando, digite novamente.')

##=================================================== MOVE AS PEÇAS =======================================================##
def MovePeças(jogador, tabuleiro, moviveis):
    while True:
        try:
            jogada = input('\nDigite a posição da peça que deseja mover: ').lower()

            if not 'b' <= jogada[0] <= 'k':
                print('Por favor, escolha apenas linhas entre B e K.')
            elif not 1 <= int(jogada[1:]) <= 12:
                print('Por favor, digite o número correspondente à coluna da peça.')
            elif tabuleiro[ord(jogada[0])-97][int(jogada[1:])-1] == ' ':
                print('Não há nenhuma peça nessa posição.')
            elif tabuleiro[ord(jogada[0])-97][int(jogada[1:])-1].dono != jogador.marca:
                print('Essa peça não é sua. ', end='')
                print(jogador)
            elif tabuleiro[ord(jogada[0])-97][int(jogada[1:])-1] not in moviveis:
                print('Você pode já mexeu essa peça, ou ela pode ter entrado nesse turno.')
            else:
                linha_antiga = ord(jogada[0])-97
                coluna = int(jogada[1:])-1
                if jogador.nome == 'Jogador 1':
                    if tabuleiro[linha_antiga+1][coluna] == ' ':
                        break
                    else:
                        print('Você não pode mover essa peça enquanto houver outra em seu caminho.')
                elif jogador.nome == 'Jogador 2':
                    if tabuleiro[linha_antiga-1][coluna] == ' ':
                        break
                    else:
                        print('Você não pode mover essa peça enquanto houver outra em seu caminho.')
        except:
            print('Houve um erro ao analisar o seu comando, digite novamente.')

    while True:
        try:          
            jogada = int(input('\nDeseja mover 1 ou 2 quadrados? \n'))

            if not 1 <= jogada <= 2:
                print('Por favor, escolha apenas entre 1 e 2')
            
            elif jogador.nome == 'Jogador 1':
                if tabuleiro[linha_antiga+jogada][coluna] == ' ':
                    linha_nova = linha_antiga + jogada
                    tabuleiro[linha_nova][coluna] = tabuleiro[linha_antiga][coluna]
                    tabuleiro[linha_nova][coluna].posiçao[0] = [linha_nova]
                    tabuleiro[linha_antiga][coluna] = ' '
                    moviveis.remove(tabuleiro[linha_nova][coluna])
                    break
                else:
                    print('Essa posição já está ocupada.')
                    
            elif jogador.nome == 'Jogador 2':
                if tabuleiro[linha_antiga-jogada][coluna] == ' ':
                    linha_nova = linha_antiga - jogada
                    tabuleiro[linha_nova][coluna] = tabuleiro[linha_antiga][coluna]
                    tabuleiro[linha_nova][coluna].posiçao[0] = [linha_nova]
                    tabuleiro[linha_antiga][coluna] = ' '
                    moviveis.remove(tabuleiro[linha_nova][coluna])
                    break
                else:
                    print('Essa posição já está ocupada.')
                
        except:
            print('Houve um erro ao analisar o seu comando, digite novamente.')

##================================================= FAZ AÇÕES COM AS PEÇAS ================================================##
def FazAtaques(jogador, tabuleiro, usaveis):
    while True:
        try:
            peça = input('\nDigite a posição da peça que deseja utilizar: ').lower()

            if not 'b' <= peça[0] <= 'k':
                print('Por favor, escolha apenas as linhas B e K.')
            elif not 1 <= int(peça[1:]) <= 12:
                print('Por favor, digite apenas os número correspondente à coluna da peça.')
            elif tabuleiro[ord(peça[0])-97][int(peça[1:])-1] == ' ':
                print('Não há nenhuma peça nessa posição.')
            elif tabuleiro[ord(peça[0])-97][int(peça[1:])-1].dono != jogador.marca:
                print('Essa peça não é sua. ', end='')
                print(jogador)
            elif tabuleiro[ord(peça[0])-97][int(peça[1:])-1] not in usaveis:
                print('Você já usou essa peça.')
            else:
                linha = ord(peça[0])-97
                coluna = int(peça[1:])-1
                alvos = tabuleiro[linha][coluna].PossiveisAlvos(tabuleiro)
                if alvos != []:
                    ataque_especial = 'não'
                    if tabuleiro[linha][coluna].especial == 5:
                        while True:
                            try:
                                ataque_especial = input('O ataque especial dessa peça está pronto, deseja usá-lo? \n').lower()

                                if ataque_especial[0] == 's':
                                    ataque_especial = 'sim'
                                    break
                                elif ataque_especial[0] == 'n':
                                    ataque_especial = 'não'
                                    break
                                else:
                                    print('Por favor, digite apenas sim ou não.')
                            except:
                                print('Houve um erro ao analisar a sua resposta, digite novamente.')
                    break
                else:
                    print('Essa peça não pode atacar ninguém.')
        except:
            print('Houve um erro ao analisar o seu comando, digite novamente.')

    if ataque_especial == 'sim' and tabuleiro[linha][coluna].classe == 'Mago':
        tabuleiro[linha][coluna].especial = 0
        
        for alvo in alvos:
            dano = tabuleiro[linha][coluna].AtaqueEspecial()
            alvo.vida -= dano
            print('{} deu {} de dano ao {} em {}!'.format(tabuleiro[linha][coluna].classe, dano, alvo.classe, chr(alvo.posiçao[0][0]+97)+str(alvo.posiçao[1][0]+1)))
            if alvo.vida <= 0:
                print('O {} em {} morreu!'.format(alvo.classe, chr(alvo.posiçao[0][0]+97)+str(alvo.posiçao[1][0]+1)))
                for linhas in tabuleiro:
                    for retira in linhas:
                        if retira == alvo:
                            linhas[linhas.index(retira)] = ' '

            else:
                print('O {} em {} ficou com {} de vida!'.format(alvo.classe, chr(alvo.posiçao[0][0]+97)+str(alvo.posiçao[1][0]+1), alvo.vida))
    else:
        while True:
            try:
                alvo = input('\nDigite a posição da peça que deseja atacar: ')

                if not 'b' <= alvo[0] <= 'k':
                    print('Por favor, escolha apenas linhas entre B e K.')
                elif not 1 <= int(alvo[1:]) <= 12:
                    print('Por favor, digite apenas o número correspondente à coluna da peça.')
                elif tabuleiro[ord(alvo[0])-97][int(alvo[1:])-1] == ' ':
                    print('Não há nenhuma peça nessa posição.')
                elif tabuleiro[ord(alvo[0])-97][int(alvo[1:])-1].dono == jogador.marca:
                    print('Essa peça é sua. ', end='')
                    print(jogador)
                elif tabuleiro[ord(alvo[0])-97][int(alvo[1:])-1] not in alvos:
                    print('A peça que você escolheu não pode atacar essa peça.')
                else:
                    if ataque_especial == 'não':
                        dano = tabuleiro[linha][coluna].AtaqueNormal()
                        if tabuleiro[linha][coluna].especial < 5:
                            tabuleiro[linha][coluna].especial += 1
                    elif ataque_especial == 'sim':
                        dano = tabuleiro[linha][coluna].AtaqueEspecial()
                        tabuleiro[linha][coluna].especial = 0
                        
                    tabuleiro[ord(alvo[0])-97][int(alvo[1:])-1].vida -= dano
                    print('{} em {} deu {} de dano ao {} em {}!'.format(tabuleiro[linha][coluna].classe, chr(tabuleiro[linha][coluna].posiçao[0][0]+97)+str(tabuleiro[linha][coluna].posiçao[1][0]+1), dano, tabuleiro[ord(alvo[0])-97][int(alvo[1:])-1].classe, alvo))

                    if tabuleiro[ord(alvo[0])-97][int(alvo[1:])-1].vida <= 0:
                        print('O {} em {} morreu!'.format(tabuleiro[ord(alvo[0])-97][int(alvo[1:])-1].classe, alvo))
                        for linhas in tabuleiro:
                            for retira in linhas:
                                if retira == tabuleiro[ord(alvo[0])-97][int(alvo[1:])-1]:
                                    linhas[linhas.index(retira)] = ' '
                    else:
                        print('O {} em {} ficou com {} de vida!'.format(tabuleiro[ord(alvo[0])-97][int(alvo[1:])-1].classe, alvo, tabuleiro[ord(alvo[0])-97][int(alvo[1:])-1].vida))

                    break

            except:
                print('Houve um erro ao analisar o seu comando, digite novamente.')

    usaveis.remove(tabuleiro[linha][coluna])
            
                
if __name__ == '__main__':
    print('Deu certo!')
