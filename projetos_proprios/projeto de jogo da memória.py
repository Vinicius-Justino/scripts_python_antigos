from random import randint
from time import sleep

print('Este programa irá gerar 5 números aleatórios entre 1 e 30')
print('\nVocê deve decorar os números exibidos em 5 segundos e depois escreve-los')
print('na ordem em que foram exibidos.')
input('\nAperte START para começar')

n1 = randint(1, 30)
n2 = randint(1, 30)
n3 = randint(1, 30)
n4 = randint(1, 30)
n5 = randint(1, 30)

print('{:5} {:5} {:5} {:5} {:5}'.format(n1, n2, n3, n4, n5))
sleep(5.0)

#???????????????????
