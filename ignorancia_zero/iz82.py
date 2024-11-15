m = int(input('digite o tamanho da sua lista: '))
n = int(input('digite quantos desses números quer somar: '))
print('')
lista = []

for numeros in range(1, m+1):
    lista += [int(input('digite o {}º número da lista: '.format(numeros)))]

soma = 0

for somas in range(0, (len(lista))):
    soma += lista[somas]
    if somas+1 == n:
        break

print('')
print('a soma dos {} primeiros números dessa lista é {}.'.format(n, soma))
