#DETERMINANDO A ÁREA A SER PINTADA
area = input('digite a área em m² a ser pintada: ')

#VERIFICANDO SE É NÚMERO
while area.isnumeric() == False:
    if '.' in area:
        if area.islower() == False:
            if area.isupper() == False:
                break
            else:
                print('esse não é um valor válido, digite novamente.')
                area = input('digite a área a ser pintada (em m²): ')
        else:
            print('esse não é um valor válido, digite novamente.')
            area = input('digite a área a ser pintada (em m²): ')
    else:
        print('esse não é um valor válido, digite novamente.')
        area = input('digite a área a ser pintada (em m²): ')

#CONVERTENDO
if area.isnumeric() == True:
    area = int(area)
else:
    area = float(area)

#DETERMINANDO A QUANTIDIDADE DE LATAS DE TINTA NECESSÁRIA
litros = area//3
resto1 = litros%3
if resto1 != 0:
    litros = litros+1
if litros < 18:
    latas = 1
elif litros > 18:
    latas = litros//18
    resto2 = litros%18
    if resto2 != 0:
        latas = latas+1

#CALCULANDO O PREÇO E MOSTRANDO AO USUÁRIO
preço = latas*80
print('se cada lata custa 80 reais e tem 18 litros, e cada litro pinta 3m², para pintar {}m² você precisa pagar {} reais em {} lata(s)'.format(area, preço, latas))
