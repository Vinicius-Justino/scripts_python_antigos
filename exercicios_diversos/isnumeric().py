x = input('isso é inútil: ')

y = 0
z = 0
t = 0

for isaphanumeric in range(10):
    y = str(y)
    if y in x:
        t = 1
        for isnumeric in range(10):
            z = str(z)
            decimal = '.' + z
            if decimal in x:
                t = 2
                break    
            z = int(z)
            z += 1

    if t == 1:
        print('{} é natural.'.format(x))
        break
    elif t == 2:
        print('{} é decimal.'.format(x))
        break

    y = int(y)
    y += 1

if t == 0:
    print('{} é alfanumérico.'.format(x))


