print('M - matituno')
print('V - Vespertino')
print('N - noturno')
while True:
    turno = input('\nDigite o turno em que você estuda: ')

    if turno == 'm' or turno == 'M':
        print('Bom Dia!')
        break
    elif turno == 'v' or turno == 'V':
        print('Boa Tarde!')
        break
    elif turno == 'n' or turno == 'N':
        print('Boa Noite!')
        break
    else:
        print('Entrada Inválida.')
