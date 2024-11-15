a = int(input('digite um número inteiro: '))
b = int(input('digite outro número inteiro: '))
c = float(input('digite um número real: '))

conta1 = (a*2)*(b/2)
conta2 = a*3 + c
conta3 = c**3

print('')
print('({}x2)x({}/2) = {}'.format(a, b, conta1))
print('{}x3 + {} = {}'.format(a, c, conta2))
print('{}³ ={}'.format(c, conta3))
