import random

print('escolha uma das portas e tente ganhar o prêmio.')
print('')
print('porta 1     porta 2     porta 3')
print(' _____       _____       _____ ')
print('|     |     |     |     |     |')
print('|     |     |     |     |     |')
print('|    º|     |    º|     |    º|')
print('|_____|     |_____|     |_____|')
print('')

r = int(input('digite o número da sua porta: '))

if r == 1:
    e = random.randint(2, 3)
    if e == 2:
        f = 3

    elif e == 3:
        f = 2

elif r == 2:
    e = random.randint(1, 3)
    if e == 1:
        f = 3

    elif e == 3:
        f = 1

elif r == 3:
    e = random.randint(1, 2)
    if e == 1:
        f = 2

    elif e == 2:
        f = 1

print('')
print('o apresentador abriu a {}ª porta e ela está errada.'.format(e))
print('')
print('agora o apresentador vai abrir a porta {}, quer trocar para a {}?'.format(r, f))
print('sim/não')
t = input('R: ')
if t == 'sim':
    aux = r
    r = f
    f = aux

    c = random.choice([r, f])
    if c == r:
        print('')
        print('a porta {} estava errada, você ganhou!'.format(f))

    else:
        print('')
        print('a porta {} estava correta, você perdeu.'.format(f))

elif t == 'não':
    c = random.choice([r, f])
    if c == r:
        print('')
        print('a porta {} estava correta, você ganhou!'.format(r))

    else:
        print('')
        print('a porta {} estava errada, você perdeu.'.format(r))
        
