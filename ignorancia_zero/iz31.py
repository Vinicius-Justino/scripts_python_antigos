i = int(input('digite um número: '))
j = int(input('digite outro número: '))
div = 1

while True:
    if div > i or div > j:
        break
    
    if j%div == 0 and i%div == 0:
        print(div)

    div += 1
