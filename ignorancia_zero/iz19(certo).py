s = input('digite o tamanho da sequência: ')
while True:
    if s.isnumeric() == False:
        print('não é um valor válido, digite novamente.')
        s = input('digite o tamanho da sequência: ')

    elif s.isnumeric() == True:
        s = int(s)
        if s > 0:
            break
        else:
            print('não é um valor válido, digite novamente.')
            s = input('digite o tamanho da sequência: ')
        
cont = 0
soma = 0

while cont < s:
    n = input('digite um número: ')
    while True:
        if n.isnumeric() == False:
            print('não é um valor válido, digite novamente.')
            n = input('digite um número: ')

        elif n.isnumeric() == True:
            n = int(n)
            if n >= 0:
                break
        else:
            print('não é um valor válido, digite novamente.')
            s = input('digite um número: ')

    n = int(n)
            
    if n%2 == 0:
        print('{}+{}={}'.format(soma, n, soma+n))
        soma += n
    cont += 1
    
