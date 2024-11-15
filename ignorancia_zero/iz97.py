frase = input('digite uma frase: ') + ' '

l = []
p = ''
for car in frase:
    if car == ' ':
        l += [p]
        p = ''

    elif car != ' ':
        p += car

print(l)
