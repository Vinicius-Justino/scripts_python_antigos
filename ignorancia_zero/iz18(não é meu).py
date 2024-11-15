n = int(input('digite um número: '))
d = 1
soma = 0

while d < n:
    if n%d == 0:
        soma += d
    d += 1

if soma == n:
    print('{} é perfeito.'.format(n))

else:
    print('{} não é perfeito.'.format(n))
