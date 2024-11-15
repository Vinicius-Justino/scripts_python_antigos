lista = []
par = []
impar = []

for numeros in range(1, 21):
    numero = int(input('digite o número {}: '.format(numeros)))
    lista += [numero]

    if numero%2 == 0:
        par += [numero]

    else:
        impar += [numero]

print('todos os números: {}'.format(lista))
print('os que são pares: {}'.format(par))
print('os que são ímpares: {}'.format(impar))
