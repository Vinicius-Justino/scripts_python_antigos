class quadrado(object):
    def __init__(self, lado=1):
        quadrado.lado = lado
    def mudaLado(novo):
        quadrado.lado = novo
    def mostraLado():
        print('\nO lado do seu quadrado é de {}'.format(quadrado.lado))
    def calculaArea():
        print('\nA área do seu quadrado é de {}.'.format(quadrado.lado*quadrado.lado))

def recebeComando():
    while True:
        açao = input('\nDeseja mudar o lado do seu quadrado(1), ver o lado(2) ou ver a área(3) \n')

        if açao == '1' or açao == '2' or açao == '3':
            return açao
        else:
            print('Escolha apenas entre as 3 opções abaixo.')

def verificaSaida(saida):
    erro = False
    for char in saida:
        if not '1' <= char <= '9' and not '.':
            print('Valor inválido, o valor do lado será 1.')
            valor = 1
            erro = True
            break

    if erro == False:
        valor = int(saida)

    return valor

lado = input('\nDigite o valor do lado do seu quadrado: ')
quadrado(verificaSaida(lado))

while True:
    comando = recebeComando()

    if comando == '1':
        novo = input('\nDigite o novo valor do lado: ')
        quadrado.mudaLado(verificaSaida(novo))

    elif comando == '2':
        quadrado.mostraLado()

    elif comando == '3':
        quadrado.calculaArea()
        
