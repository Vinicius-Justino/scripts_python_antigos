print('--------------------------------CALCULADORA------------------------------------')
print('operações:')
print('+ = adição')
print('- = subtrução')
print('* = multiplicação')
print('/ = divisão')
print('** = potência')
print('// = radiciação (raiz quadrada)')
while True:
	n1 = float(input('primeiro número:'))
	sinal = str(input('operação:'))
	if sinal == '+':
		n2 = float(input('segundo número:'))
		print('{}{}{}={}'.format(n1, sinal, n2, n1+n2))
	if sinal == '-':
		n2 = float(input('segundo número:'))
		print('{}{}{}={}'.format(n1, sinal, n2, n1-n2))
	if sinal == '*':
		n2 = float(input('segundo número:'))
		print('{}{}{}={}'.format(n1, sinal, n2, n1*n2))
	if sinal == '/':
		n2 = float(input('segundo número:'))
		print('{}{}{}={}'.format(n1, sinal, n2, n1/n2))
	if sinal == '**':
		n2 = float(input('segundo número:'))
		print('{}{}{}={}'.format(n1, sinal, n2, n1**n2))
	if sinal == '//':
		print('{}{}={}'.format(n1, sinal, n1**(1/2)))
