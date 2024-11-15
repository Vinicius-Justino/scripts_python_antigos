#DETERMINANDO N
n = input('digite um número: ')

while n.isnumeric() == False:
    print('não é um valor válido, digite novamente.')
    n = input('digite um número: ')

n = int(n)

#MÁGICA
impar = 1

while n > 0:
    print(impar)
    impar = impar + 2
    n = n - 1
