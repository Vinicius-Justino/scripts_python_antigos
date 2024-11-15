#determinando a tabuada
numeros = int(input('digite quantos números vai multiplicar: '))
começo = int(input('digite o número em que vai começar a tabuada: '))
fim = int(input('digite o número em que vai terminar a tabuada: '))

#tabuada
#numeros
for tabuada in range(numeros):    #para cada número loop isso:
    print('')
    print('número {}:'.format(tabuada+1))
    print('')
    for contas in range(começo, fim+1):    #para cada conta loop isso:
        print('{}x{}={}'.format(tabuada+1, contas, (tabuada+1)*(contas)))
