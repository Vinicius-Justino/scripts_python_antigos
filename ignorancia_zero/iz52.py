lista = []
n = int(input('digite o 1º número: '))
if n > 10:
    lista += [n]
cont = 1
while n != -1:
    n = int(input('digite o {}º número: '.format(cont+1)))

    if n == -1:
        break

    elif n > 10:
        lista += [n]

    cont += 1

print('')
print('os números maiores que 10 dessa listas são:')
print(lista)
