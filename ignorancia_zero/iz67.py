def conversor():
    horas = int(input('digite as horas:'))
    minutos = int(input('digite os minutos: '))
    
    if horas >= 13:
        horas -= 12
        print('{}:{} P.M.'.format(horas, minutos))

    else:
        print('{}:{} A.M.'.format(horas, minutos))

while True:
    conversor()
    print('')
