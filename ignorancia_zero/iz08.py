#DETERMINADO A ÁREA A SER PINTADA
area = input('digite a área em m² a ser pintada: ')

#VERIFICANDO SE É NÚMERO
while area.isnumeric() == False:
    print('esse não é um valor válido, digite novamente.')
    area = input('digite a área em m² a ser pintada: ')

#CONVERTENDO
area = int(area)

#LITROS USADOS
litros = area//6
resto_litros = area%6
if resto_litros != 0:
    litros = litros+1

folga = litros/10
while True:
    folga = folga+0.01
    comparaçao = str(folga)
    if '.0' in comparaçao:
        break

litros = litros + folga

#PREÇO EM LATAS
latas = litros//18
resto_latas = litros%18
if resto_latas != 0:
    latas = latas+1
preço_latas = 80*latas

#PREÇO EM GALÕES
galoes = litros//4
resto_galoes = litros%4
if resto_galoes != 0:
    galoes = galoes+1
preço_galoes = 25*galoes

#PREÇO MISTURADO
misto1 = litros//18
resto1_misto = litros%18
misto2 = 0
if resto1_misto != 0:
    misto2 = resto1_misto//4
    resto2_misto = resto1_misto%4
    if resto2_misto != 0:
        misto2 = misto2+1
preço_misto = misto1*80+misto2*25

#MOSTRANDO OS RESULTADOS
print('latas têm 18 litros de tinta e custam 80 reais.')
print('galões têm 4 litros de tinta e custam 25 reais.')
print('cada litro de tinta pinta 6m².')
print('pintado essa área com apenas latas, você usará {} latas e pagará {} reais'.format(latas, preço_latas))
print('pintando essa área com apenas galões, você usará {} galões e pagará {} reais'.format(galoes, preço_galoes))
print('utilizando tanto latas quanto galões, você usará {} latas e {} galões, e pagará {} reais'.format(misto1, misto2, preço_misto))
