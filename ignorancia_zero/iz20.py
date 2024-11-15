n = int(input('digite um número maior que 10: '))
aux = n
dig = 0
rev = ''

while aux != 0:
    aux = aux//10
    dig = aux%10
    rev += str(dig)
    print(aux)
    print(dig)
    print(rev)
    print(n)

rev = int(rev)

if rev == n:
    print('é palindrome.')

else:
    print('não é palindrome.')
