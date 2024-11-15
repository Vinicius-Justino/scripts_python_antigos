n = int(input('digite um número maior que 1: '))
aux = 1
copia = n
soma = 0

while copia != 0:
    soma += aux/copia
    print('{} += {}/{}'.format(soma, aux, copia))
    aux += 1
    copia -= 1
