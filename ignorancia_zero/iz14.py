#DETERMINANDO N
n = input('digite um número: ')

while n.isnumeric() == False:
    print('não é um valor válido, digite novamente.')
    n = input('digite um número: ')

n = int(n)

while n <= 0:
    print('esse não é um valor válido, digite novamente.')
    n1 = input('digite um número: ')
    teste = str(n1)
    while teste.isnumeric() == False:
        print('não é um valor válido, digite novamente.')
        n = input('digite um número: ')

#EXECUTANDO
conta1 = 0
conta2 = 1
resultado = conta1+conta2
n = n-1

print('{}+{}={}'.format(conta1, conta2, resultado))

conta1 = resultado
conta2 = conta2+1
resultado = conta1+conta2
n = n-1

while n != 0:
    print('{}+{}={}'.format(conta1, conta2, resultado))
    conta1 = resultado
    conta2 = conta2+1
    resultado = conta1+conta2
    n = n-1

print('{}+{}={}'.format(conta1, conta2, resultado))
    
