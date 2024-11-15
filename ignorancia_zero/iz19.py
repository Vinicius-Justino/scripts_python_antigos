n = input('digite um número: ')

while n.isnumeric() == False:
    print('não é um valor válido, digite novamente.')
    n = input('digite um número: ')

n = int(n)

cont = 0
par = 2
soma = 0

while cont <= n:
    cont += 2

    if cont > n:
        break

    print('{}+{}={}'.format(soma, par, soma+par))
    soma += par
    par += 2

print()
    
