# PARA TERMINAR
# - VER SE PRECISA DE MAIS ALGUMA FUNÇÃO, E CRIÁ-LA.
# - ARRUMAR POSSÍVEIS PROBLEMAS.

from random import choice

if __name__ == '__main__':
    from classes import *

else:
    from peças.classes import *

##============================= PEÇAS CRIADAS ================================##
CajadoDeFogo = item('Cajado de Fogo', 15, 'ataque', 'Arma', '♥')
EspadaCurta = item('Espada Curta', 5, 'ataque', 'Arma', '♠')
ArcoDeMadeira = item('Arco de madeira', 10, 'ataque', 'Arma', '♣')
PoçaoDeCura = item('Poção de cura', 20, 'vida', 'Poção', '♠, ♣, e ♥')

##============================== CRIA URNAS ==================================##
def CriaUrna(dono):
    urna = []
    
    for cria_magos in range(10):
        urna += ['Mago']       
    for cria_soldados in range(30):
        urna += ['Soldado']
    for cria_elfos in range(20):
        urna += ['Elfo']
    for cria_poçoes_cura in range(40):
        urna += ['Poção de cura']

    return urna

##============================== SACA PEÇAS ==================================##
def SacaPeça(urna, jogador_atual, tabuleiro):
    peça = choice(urna)

    if JogadaPossivel(ConvertePeça(peça, jogador_atual), jogador_atual, tabuleiro):
        urna.remove(peça)
        return peça
    else:
        SacaPeça(urna, jogador_atual, tabuleiro)

##=========================== CONVERTE AS PEÇAS ==============================##
def ConvertePeça(peça, dono):
    soldado = guerreiro(EspadaCurta, dono)
    mago = conjurador(CajadoDeFogo, dono)
    arqueiro = elfo(ArcoDeMadeira, dono)
    PoçaoDeCura = item('Poção de cura', 20, 'vida', 'Poção', '♠, ♣, e ♥')
    
    peças = [soldado, mago, arqueiro, PoçaoDeCura]

    for equivalente in peças:
        try:
            if peça == equivalente.nome:
                return equivalente
        except:
            if peça == equivalente.classe:
                equivalente.arma.Efeito(equivalente)
                return equivalente

##===================== RETORNA AS PEÇAS AO NORMAL ===========================##
def RetornaPeça(peça):
    try:
        return peça.nome
    except:
        return peça.classe        

##================= VERIFICA SE A PEÇA SACADA TEM UTILIDADE ==================##
def JogadaPossivel(peça, jogador, tabuleiro):
    if peça.classe == 'Mago' or peça.classe == 'Soldado' or peça.classe == 'Elfo':
        return True
    
    tropa = []
    for pega_peças1 in tabuleiro:
        for pega_peças2 in pega_peças1:
            try:
                if pega_peças2.dono == jogador.marca:
                    tropa += [pega_peças2]
            except:
                continue

    incompativeis = []
    for incompativel in tropa:
        if incompativel.tipo not in peça.tipos:
            incompativeis += [incompativel]

    for elimina in incompativeis:
        tropa.remove(elimina)

    if tropa == []:
        return False

    possiveis = 0
    if peça.classe == 'Arma':
        for confere in tropa:
            if confere.arma.nome != peça.nome:
                possiveis += 1
    elif peça.classe == 'Item':
        for confere in tropa:
            try:
                if confere.item.nome != peça.nome:
                    possiveis += 1
            except:
                continue
    elif peça.classe == 'Poção':
        for confere in tropa:
            if confere.poçao == False:
                possiveis += 1

    if possiveis != 0:
        return True

    elif possiveis == 0:
        return False

##============================ ATAQUE POSSÍVEL ===============================##
def AtaquesPossiveis(jogador, tabuleiro):
    usaveis = []
    tropa = []
    for reune1 in tabuleiro:
        for reune2 in reune1:
            try:
                if reune2.dono == jogador.marca and reune2.classe != 'Dragão':
                    tropa += [reune2]
            except:
                continue

    for verifica in tropa:
        alcance = verifica.PossiveisAlvos(tabuleiro)
        if alcance != []:
            usaveis += [verifica]
            
    return usaveis

##========================== MOVIMENTOS POSSIVEIS ============================##
def MovimentosPossiveis(jogador, tabuleiro):
    tropa = []
    for reune1 in tabuleiro:
        for reune2 in reune1:
            try:
                if reune2.dono == jogador.marca:
                    if reune2.classe != 'Dragão':
                        tropa += [reune2]
            except:
                continue

    for elimina in tropa:
        if jogador.nome == 'Jogador 1':
            if tabuleiro[elimina.posiçao[0][0]+1][elimina.posiçao[1][0]] != ' ':
                tropa.remove(elimina)
        elif jogador.nome == 'Jogador 2':
            if tabuleiro[elimina.posiçao[0][0]-1][elimina.posiçao[1][0]] != ' ':
                tropa.remove(elimina)

    moviveis = tropa.copy()

    return moviveis

if __name__ == '__main__':
    jogador1 = jogador('Jogador1', '☺', 0)
    urna = CriaUrna(jogador1)
    
    print('Deu certo!')
