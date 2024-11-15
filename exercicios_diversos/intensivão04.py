print('segue a lista dos números de 4 algarismos cuja rais quadrada é \nigual a soma de si mesmo divido em duas dezenas:')
n = 1000
while n < 10000:
    d1 = n//100
    d2 = n%100

    if n**(1/2) == d1 + d2:
        print(n)

    n +=1
