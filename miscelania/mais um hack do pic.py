divisores = []

n = 1

while len(divisores) != 8:
    if 2015%n == 0:
        divisores += [n]

    n += 1

for mostra in divisores:
    print(mostra, end='  ')
