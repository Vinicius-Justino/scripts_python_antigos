p = float(input('preço do produto:'))
print('esse valor à vista equivale a R${:.2f} \ne parcelado esse valor é de R${:.2f}'.format(p-(p*10/100), p+(p*8/100)))
