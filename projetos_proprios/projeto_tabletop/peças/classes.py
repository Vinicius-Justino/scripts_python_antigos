from random import randint
from random import choice
##============================= CLASSE JOGADOR ===============================##
class jogador(object):
    def __init__(self, nome, marca, começo):
        self.nome = nome
        self.marca = marca
        self.começo = começo
        self.urna = None
        self.dragao = None
    def __str__(self):
        return 'As suas peças estão marcadas com o símbolo {}.'.format(self.marca)

##=========================== CLASSE CONJURADOR ==============================##
class conjurador(object):
    def __init__(self, arma, dono):
        self.classe = 'Mago'
        self.tipo = '♥'
        self.dono = dono.marca
        self.ataque = 5
        self.mira = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0]
        self.vida = 60
        self.arma = arma
        self.especial = 0
        self.status = 'Normal'
        self.item = None
        self.poçao = False
        self.posiçao = [None, None]
    def AtaqueNormal(self):
        multiplicador = choice(self.mira)
        dano = randint(10, self.ataque)
        return dano*multiplicador
    def AtaqueEspecial(self):
        dano = randint(13, self.ataque+3)
        return dano
    def PossiveisAlvos(self, tabuleiro):
        alvos = []
        
        alcance = [[self.posiçao[0][0]+1, self.posiçao[1][0]], [self.posiçao[0][0]+2, self.posiçao[1][0]],
                   [self.posiçao[0][0]-1, self.posiçao[1][0]], [self.posiçao[0][0]-2, self.posiçao[1][0]],
                   [self.posiçao[0][0], self.posiçao[1][0]-1], [self.posiçao[0][0], self.posiçao[1][0]-2],
                   [self.posiçao[0][0], self.posiçao[1][0]+1], [self.posiçao[0][0], self.posiçao[1][0]+2],
                   [self.posiçao[0][0]+1, self.posiçao[1][0]+1], [self.posiçao[0][0]+1, self.posiçao[1][0]-1],
                   [self.posiçao[0][0]-1, self.posiçao[1][0]+1], [self.posiçao[0][0]-1, self.posiçao[1][0]-1]]

        for pos in alcance:
            try:
                if pos[0] < 0 or pos[0] > 11:
                    raise IndexError
                elif pos[1] < 0 or pos[1] > 11:
                    raise IndexError

                alvos += [tabuleiro[pos[0]][pos[1]]]
            except:
                alvos += ' '
                
        while ' ' in alvos:
            alvos.remove(' ')

        aliados = []
        for peça in range(len(alvos)):
            if alvos[peça].dono == self.dono:
                aliados += [alvos[peça]]

        for aliado in aliados:
            alvos.remove(aliado)

        return alvos

'''     
            | 2/0 |                                        linha     coluna
      | 1/-1| 1/0 | 1/1 |                                    0    /    0
| 0/-2| 0/-1| 0/0 | 0/1 | 0/2 | <= Alcance do conjurador
      |-1/-1|-1/0 |-1/1 |
            |-2/0 |
'''

##============================ CLASSE GUERREIRO ==============================##
class guerreiro(object):
    def __init__(self, arma, dono):
        self.classe = 'Soldado'
        self.tipo = '♠'
        self.dono = dono.marca
        self.ataque = 10
        self.mira = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0]
        self.vida = 70
        self.arma = arma
        self.especial = 0
        self.status = 'Normal'
        self.item = None
        self.poçao = False
        self.posiçao = [None, None]
    def AtaqueNormal(self):
        multiplicador = choice(self.mira)
        dano = randint(7, self.ataque)
        return dano*multiplicador
    def AtaqueEspecial(self, tabuleiro):
        dano = randint(7, self.ataque)
        return dano*2
    def PossiveisAlvos(self, tabuleiro):
        alvos = []

        alcance = [[self.posiçao[0][0]+1, self.posiçao[1][0]], [self.posiçao[0][0]-1, self.posiçao[1][0]],
                   [self.posiçao[0][0], self.posiçao[1][0]+1], [self.posiçao[0][0], self.posiçao[1][0]-1]]

        if self.arma.nome == 'Espada Longa':
            alcance += [[self.posiçao[0][0]+1, self.posiçao[1][0]+1], [self.posiçao[0][0]-1, self.posiçao[1][0]+1],
                        [self.posiçao[0][0]+1, self.posiçao[1][0]-1], [self.posiçao[0][0]-1, self.posiçao[1][0]-1]]

        for pos in alcance:
            try:
                if pos[0] < 0 or pos[0] > 11:
                    raise IndexError
                elif pos[1] < 0 or pos[1] > 11:
                    raise IndexError

                alvos += [tabuleiro[pos[0]][pos[1]]]
            except:
                alvos += ' '

        while ' ' in alvos:
            alvos.remove(' ')

        aliados = []
        for peça in range(len(alvos)): 
            if alvos[peça].dono == self.dono:
                aliados += [alvos[peça]]

        for aliado in aliados:
            alvos.remove(aliado)

        return alvos
'''
       | 1/0 |                                                  
 | 0/-1| 0/0 | 0/1 |  <= Alcance do guerreiro sem espada longa
       |-1/0 |                                                   linha   coluna
                                                                   0   /   0
 | 1/-1| 1/0 | 1/1 |
 | 0/-1| 0/0 | 0/1 |  <= Alcance do guerreiro com espada longa
 |-1/-1|-1/0 |-1/1 |
'''

##============================= CLASSE ÉLFICA ================================##
class elfo(object):
    def __init__(self, arma, dono):
        self.classe = 'Elfo'
        self.tipo = '♣'
        self.dono = dono.marca
        self.ataque = 5
        self.mira = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0]
        self.vida = 50
        self.arma = arma
        self.especial = 0
        self.status = 'Normal'
        self.item = None
        self.poçao = False
        self.posiçao = [None, None]
    def AtaqueNormal(self):
        multiplicador = choice(self.mira)
        dano = randint(7, self.ataque)
        return dano*multiplicador
    def AtaqueEspecial(self):
        dano = 0
        for flechadas in range(3):
            multiplicador = choice(self.mira)
            flecha = randint(1, 10)
            dano += flecha*multiplicador
        return max(10, dano)
    def PossiveisAlvos(self, tabuleiro):
        alvos = []

        alcance = [[self.posiçao[0][0]+1, self.posiçao[1][0]], [self.posiçao[0][0]+2, self.posiçao[1][0]],
                   [self.posiçao[0][0]+3, self.posiçao[1][0]], [self.posiçao[0][0]-1, self.posiçao[1][0]],
                   [self.posiçao[0][0]-2, self.posiçao[1][0]], [self.posiçao[0][0]-3, self.posiçao[1][0]],
                   [self.posiçao[0][0], self.posiçao[1][0]-1], [self.posiçao[0][0], self.posiçao[1][0]-2],
                   [self.posiçao[0][0], self.posiçao[1][0]+1], [self.posiçao[0][0], self.posiçao[1][0]-3],
                   [self.posiçao[0][0], self.posiçao[1][0]+2], [self.posiçao[0][0], self.posiçao[1][0]+3],
                   [self.posiçao[0][0]+1, self.posiçao[1][0]+1], [self.posiçao[0][0]+1, self.posiçao[1][0]-1],
                   [self.posiçao[0][0]-1, self.posiçao[1][0]+1], [self.posiçao[0][0]-1, self.posiçao[1][0]-1]]

        for pos in alcance:
            try:
                if pos[0] < 0 or pos[0] > 11:
                    raise IndexError
                elif pos[1] < 0 or pos[1] > 11:
                    raise IndexError

                alvos += [tabuleiro[pos[0]][pos[1]]]
            except:
                alvos += ' '

        while ' ' in alvos:
            alvos.remove(' ')

        aliados = []
        for peça in range(len(alvos)):
            if alvos[peça].dono == self.dono:
                aliados += [alvos[peça]]

        for aliado in aliados:
            alvos.remove(aliado)

        return alvos
        

'''
                  | 3/0 |
                  | 2/0 |                                   linha     coluna
            | 1/-1| 1/0 | 1/1 |                                0    /    0
| 0/-3| 0/-2| 0/-1| 0/0 | 0/1 | 0/2 | 0/3 | <= Alcance do elfo
            |-1/-1|-1/0 |-1/1 |
                  |-2/0 |
                  |-3/0 |
'''

##============================ CLASSE DRACÔNICA ==============================##
class dragao(object):
    def __init__(self, dono):
        self.classe = 'Dragão'
        self.tipo = '♦'
        self.ataque = 25
        self.vida = 100
        self.dono = dono.marca
    def Ataque(self):
        dano = randint(10, self.ataque)
        return dano
    def PossivesAlvos(self, tabuleiro):
        alvos = []

        if self.dono == '☺':
            alcance = tabuleiro[0:4]
        elif self.dono == '☻':
            alcance = tabuleiro[9:13]

        for espaços in alcance:
            for alvo in espaços:
                try:
                    if alvo.dono != self.dono:
                        alvos += [alvo]
                except:
                    pass

        return alvos
                            
'''
                          Alcance do dragão:

 | 0/-3| 0/-2| 0/-1| 0/0 | 0/0 | 0/0 | 0/0 | 0/0 | 0/0 | 0/1 | 0/2 | 0/3 |
 |-1/-3|-1/-2|-1/-1|-1/0 |-1/0 |-1/0 |-1/0 |-1/0 |-1/0 |-1/1 |-1/2 |-1/3 |
 |-2/-3|-2/-2|-2/-1|-2/0 |-2/0 |-2/0 |-2/0 |-2/0 |-2/0 |-2/1 |-2/2 |-2/3 |
 |-3/-3|-3/-2|-3/-1|-3/0 |-3/0 |-3/0 |-3/0 |-3/0 |-3/0 |-3/1 |-3/2 |-3/3 |
'''

##========================== CLASSE DOS EQUIPÁVEIS ===========================##
class item(object):
    def __init__(self, nome, melhoria, status, classe, tipos):
        self.classe = classe
        self.nome = nome
        self.melhoria = melhoria
        self.status = status
        self.tipos = tipos
    def Efeito(self, alvo):
        if self.status == 'ataque':
            alvo.ataque += self.melhoria
        if self.status == 'vida':
            alvo.vida += self.melhoria
    def __str__(self):
        if len(self.tipos) >= 2:
            return 'Esse item é compatível apenas com os tipos {}.'.format(self.tipos)
        else:
            return 'Esse item é compatível apenas com as tipos {}.'.format(self.tipos)


       
if __name__ == '__main__':
    print('Deu certo!')
