from random import randint

tabela = []

for dado in range(100):
    face = randint(1, 6)
    tabela += [face]

print('{} de 100 vezes o número 1 foi sorteado.'.format(tabela.count(1)))
print('{} de 100 vezes o número 2 foi sorteado.'.format(tabela.count(2)))
print('{} de 100 vezes o número 3 foi sorteado.'.format(tabela.count(3)))
print('{} de 100 vezes o número 4 foi sorteado.'.format(tabela.count(4)))
print('{} de 100 vezes o número 5 foi sorteado.'.format(tabela.count(5)))
print('{} de 100 vezes o número 6 foi sorteado.'.format(tabela.count(6)))
