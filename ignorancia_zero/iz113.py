class ponto:
    def __init__(self, linha, coluna):
        ponto.linha = linha
        ponto.coluna = coluna
    def imprimePosiçao(self):
        print('Linha:', ponto.linha)
        print('Coluna:', ponto.coluna)

class retangulo:
    def __init__(self, base, altura, ponto):
        retangulo.base = base
        retangulo.altura = altura
        retangulo.ponto = ponto
    def imprimeRetangulo(self):
        print(' ', end='')
        for base in range(retangulo.base):
            if base == retangulo.ponto.coluna and retangulo.ponto.linha == 1 and base != retangulo.base-1:
                print('o', end='')
            elif base == retangulo.ponto.coluna and retangulo.ponto.linha == 1 and base == retangulo.base-1:
                print('o')
            elif base != retangulo.base-1:
                print('_', end='')
            elif base == retangulo.base-1:
                print('_')
        for altura in range(1, retangulo.altura+1):
            if altura == retangulo.ponto.linha and altura != retangulo.altura:
                if retangulo.ponto.coluna == 1:
                    saida = 'o' + ' '*retangulo.base + '|'
                elif retangulo.ponto.coluna == retangulo.base:
                    saida = '|' + ' '*retangulo.base + 'o'
                else:
                    saida = '|' + ' '*(retangulo.ponto.coluna-1) + 'o' + ' '*(retangulo.base - (retangulo.ponto.coluna)) + '|'
            elif altura == retangulo.ponto.linha and altura == retangulo.altura:
                if retangulo.ponto.coluna == 1:
                    saida = 'o' + '_'*retangulo.base + '|'
                elif retangulo.ponto.coluna == retangulo.base:
                    saida = '|' + '_'*retangulo.base + 'o'
                else:
                    saida = '|' + '_'*(retangulo.ponto.coluna-1) + 'o' + '_'*(retangulo.base - (retangulo.ponto.coluna)) + '|'
            elif altura != retangulo.altura:
                saida = '|' + ' '*retangulo.base + '|'
            else:
                saida = '|' + '_'*retangulo.base + '|'
            print(saida)

base = int(input('Digite o tamanho da base do retângulo: '))
altura = int(input('Digite o tamanho da altura do retângulo: '))

ponto = ponto(None, None)
retangulo = retangulo(base, altura, ponto)

while True:
    print('\nO que deseja fazer:')
    açao = input('ver o seu retângulo(1)  mudar as medidas(2)  marcar um ponto(3)  ver a posição do ponto(4) \n')

    if açao == '1':
        retangulo.imprimeRetangulo()

    elif açao == '2':
        base = int(input('Digite o tamanho da nova base: '))
        altura = int(input('Digite o tamanho da nova altura: '))
        retangulo.base = base-1
        retangulo.altura = altura-1

    elif açao == '3':
        linha = int(input('Digite a linha do ponto: '))
        coluna = int(input('Digite a coluna do ponto: '))
        retangulo.ponto.linha = linha
        retangulo.ponto.coluna = coluna

    elif açao == '4':
        retangulo.ponto.imprimePosiçao()

    else:
        print('Não entendi como um comando.')
