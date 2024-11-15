lista = []

n = int(input('digite o 1º número: '))

if n%2 == 0:
    lista += [n]

cont = 1

while n != -1:
    n = int(input('digite o {}º número: '.format(cont+1)))

    if n == -1:
        break

    elif n%2 == 0:
        lista += [n]

    cont += 1

print('')
print('os números pares dessa sequência são:')
print(lista)
