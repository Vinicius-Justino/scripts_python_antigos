reais = float(input('Quanto dinheiro você tem? \nR$ '))
dolares = reais/5.26
euros = reais/5.70
ienes = reais/0.049

print('\nCom R${:.2f}, você pode comprar US${:.2f}, ou €{:.2f}, ou ¥{:.2f}.'.format(reais, dolares, euros, ienes))
