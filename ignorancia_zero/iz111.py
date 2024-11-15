class retangulo(object):
    def __init__(self, base, altura):
        retangulo.base = base
        retangulo.altura = altura
    def mudaLados(self, nova_base, nova_altura):
        retangulo.base = nova_base
        retangulo.altura = nova_altura
    def mostraLados(self):
        print('A base do seu triângulo é {} e a altura é {}.'.format(retangulo.base, retangulo.altura))
    def calculaPerimetro(self):
        print('O perímetro do seu retângulo é {}.'.format((retangulo.base*2) + (retangulo.altura*2)))
    def calculaArea(self):
        print('A área do seu retângulo é {}.'.format(retangulo.base*retangulo.altura))
    def calculaPisos(self, tamanho):
        pisos = (retangulo.base*retangulo.altura)//tamanho
        if (retangulo.base*retangulo.altura)%tamanho:
            pisos += 1
            
        print('Você precisará de aproximandamente {} pisos para cobrir a área do seu retângulo.'.format(pisos))

def recebeComando():
    while True:
        print('\nO que deseja fazer com o retângulo:')
        comando = input('Mudar os lados(1), ver os lados(2), ver o perímetro(3), ver a área(4), colocar piso(5) \n')

        if comando == '1' or comando == '2' or comando == '3' or comando == '4' or comando == '5':
            return comando
        else:
            print('Por favor, escolha apenas entre as 5 opções abaixo.')

def recebeBase(base):
    erro = False
    for char in base:
        if not '0' <= char <= '9' and not char == '.':
            print('Valor inválido, o valor da base será 2.')
            valor = 2
            erro = True
            break

    if erro == False:
        valor = int(base)

    return valor

def recebeAltura(altura):
    erro = False
    for char in altura:
        if not '0' <= char <= '9' and not char == '.':
            print('Valor inválido, o valor da altura será 1.')
            valor = 2
            erro = True
            break

    if erro == False:
        valor = int(altura)

    return valor

def recebePiso():
    pisos = input('Digite o tamanho do lado do piso: ')

    erro = False
    for char in pisos:
        if not '1' <= char <= '9':
            print('Valor inválido,  tamanho do piso será 1.')
            valor = 1
            erro = True
            break

    if erro == False:
        valor = int(pisos)

    return valor

base = input('Digite o tamanho da base do seu triângulo: ')
base = recebeBase(base)

altura = input('Digite o tamanho da altura do seu triângulo: ')
altura = recebeAltura(altura)

retangulo = retangulo(base, altura)

while True:
    comando = recebeComando()

    if comando == '1':
        base = input('Digite o novo tamanho da base: ')
        base = recebeBase(base)

        altura = input('Digite o novo tamanho da altura: ')
        altura = recebeAltura(altura)

        retangulo.mudaLados(base, altura)

    elif comando == '2':
        retangulo.mostraLados()

    elif comando == '3':
        retangulo.calculaPerimetro()

    elif comando == '4':
        retangulo.calculaArea()

    elif comando == '5':
        piso = recebePiso()
        retangulo.calculaPisos(piso)
        
    
