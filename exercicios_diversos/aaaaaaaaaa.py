x = input('isso é inútil: ')

y = 0

for isnumeric in range(10):
    y = str(y)
    if y in x:
        print('tem número')
        break
    y = int(y)
    y += 1
