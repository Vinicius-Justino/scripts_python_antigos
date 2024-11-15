def potencia(x):
    '''
função potência
pega um número x e eleva a N
    '''
    def expoente(N):
        '''
    função expoente
    escolhe um número N qualquer
        '''
        print(x**N)

    return expoente

a = potencia(3)

a(1)
a(2)
a(3)
a(4)
a(5)
a(6)
