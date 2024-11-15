n = int(input('digite um número: '))
cont = 0

#determinando os primos
for teste in range(2, n+1):
    for primo in range(2, teste+1):
        if teste > 2 and teste%2 == 0:
            break
        
        cont += 1

        if teste == primo:
            print(teste)
            break

        if teste%primo == 0:
            break

print('para que esses números fossem encontrados houveram {} comparações'.format(cont))
