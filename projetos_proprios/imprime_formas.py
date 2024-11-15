def imprimeTriangulo(lado):
    '''
Imprime um retângulo com a medida do lado equivalente ao valor fornecido.
    '''
    print('|\\')
    for altura in range(1, lado+1):
        print('|', end='')
        if altura == lado:
            for base in range(lado):
                print('_', end='')
            print('\\')
        else:
            saida = ' '*altura + '\\'
            print(saida)

def imprimeRetangulo(base, altura):
    '''
Imprime um retângulo com base e altura equivalente aos valores fornecidos.
    '''
    print(' ', end='')
    for largura in range(base):
        if largura != base-1:
            print('_', end='')
        else:
            print('_')

    for tamanho in range(altura):
        if tamanho != altura-1:
            saida = '|' + ' '*base + '|'
        else:
            saida = '|' + '_'*base + '|'

        print(saida)

if __name__ == '__main__':
    imprimeRetangulo(20, 6)
    print('')
    imprimeTriangulo(10)
