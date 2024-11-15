idade = int(input('em que ano você nasceu? R:'))
ano = int(input('em que ano você está? R:'))
idoso = ano-60
adulto = ano-18
adolescente = ano-13
if idade <= idoso:
    print('você é idoso')
elif idade <= adulto:
    print('você é adulto')
elif idade <= adolescente:
    print('você é adolescente')
else:
    print('você é uma criança')
