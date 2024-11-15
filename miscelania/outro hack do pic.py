divisores = []

for divisor in range(1, 157):
    if 104%divisor == 0 and 117%divisor == 0 and 156%divisor == 0:
        divisores += [divisor]

print('O mdc entre 104, 117 e 156 é {}.'.format(max(divisores)))
