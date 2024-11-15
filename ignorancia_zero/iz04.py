dinheiro = input('quanto você ganha por hora trabalhada? R:')
while dinheiro.isnumeric() == False:
    if '.' in dinheiro:
        if dinheiro.islower() == False:
            if dinheiro.isupper() == False:
                if dinheiro.istitle() == False:
                    break
                else:
                    print('não é um valor válido, digite novamente.')
                    dinheiro = input('quanto você ganha por hora trabalhada? R:')
            else:
                print('não é um valor válido, digite novamente.')
                dinheiro = input('quanto você ganha por hora trabalhada? R:')
        else:
            print('não é um valor válido, digite novamente.')
            dinheiro = input('quanto você ganha por hora trabalhada? R:')
    else:
        print('não é um valor válido, digite novamente.')
        dinheiro = input('quanto você ganha por hora trabalhada? R:')
dinheiro = float(dinheiro)
horas = input('quantas horas você trabalha por dia? R:')
while horas.isnumeric() == False:
    if '.' in horas:
        if horas.islower() == False:
            if horas.isupper() == False:
                if horas.istitle() == False:
                    break
                else:
                    print('não é um valor válido, digite novamente.')
                    horas = input('quantas horas você trabalha por dia? R:')
            else:
                print('não é um valor válido, digite novamente.')
                horas = input('quantas horas você trabalha por dia? R:')
        else:
            print('não é um valor válido, digite novamente.')
            horas = input('quantas horas você trabalha por dia? R:')
    else:
        print('não é um valor válido, digite novamente.')
        horas = input('quantas horas você trabalha por dia? R:')
horas = float(horas)
while horas > 15:
    if horas > 24:
        print('isso é mais que um dia, quem você pensa que eu sou?')
        horas = float(input('quantas horas você trabalha por dia? '))
    elif horas > 15:
        print('é impossível trabalhar todo esse tempo por dia. Por favor seja sincero.')
        horas = float(input('quantas horas você trabalha por dia? R:'))
    elif horas <= 15:
        break
total = dinheiro*horas
print('você ganha {} reais por dia.'.format(total))
if total >= 5000:
    if horas <= 11:
        print('eu quero seu emprego!')
    elif horas > 11:
        print('você deve ser rico!')
elif total >= 900:
    if horas <= 11:
        print('você tem um ótimo emprego!')
    elif horas > 11:
        print('você tem um bom emprego!')
elif total < 900:
    if horas <= 11:
        print('você trabalha muito mas vale à pena!')
    if horas > 11:
        print('você tem um emprego regular.')
