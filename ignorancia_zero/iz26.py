#DETERMINANDO x E y
m = int(input('digite um número: '))
n = int(input('digite outro número: '))

if m%2 == 0:
    x = m - 2

elif m%2 != 0:
    x = m - 3

if n%2 == 0:
    y = n - 2

elif n%2 != 0:
    y = n - 3

print('{}x{}-{}**2+{}={}'.format(x, y, x, y, (x*y - x**2 + y)))
