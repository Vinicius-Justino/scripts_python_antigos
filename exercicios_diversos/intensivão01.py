n = int(input('digite um número maior que 10: '))
aux = n
dig = 0
rev = ''

while aux != 0:
    dig = aux%10
    aux = aux//10
    rev += str(dig)

rev = int(rev)

print('número: {}'.format(n))
print('reverso: {}'.format(rev))

if rev == n:
    print('{} é palindrome.'.format(n))

else:
    print('{} não é palindrome.'.format(n))
