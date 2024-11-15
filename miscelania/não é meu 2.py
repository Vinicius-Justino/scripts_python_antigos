x = float(input('Insira o valor de x: '))   #angulo agudo
n = int(input('Insira o valor de n: '))     #complemento de x

cos = 0

for k in range(n):    #------
    fatorial = 1            #|
                            #|----- seno de n
    for j in range(1, k+1): #|
        fatorial *= j #------

    if k % 2 == 0 and k % 4 == 0:       #-------
        cos += ((x**k)/fatorial)               #|
                                               #|---- local de x círculo?
    elif k % 2 == 0:                           #|
        cos += (-1) * ((x**k)/fatorial) #-------
        
print('O cos({}) é igual a: {}'.format(x,cos))
