aluno = float(input('digite a altura do aluno 1: '))

cont = 2
maior = aluno
menor = aluno

amostra1 = 1
amostra2 = 1

while cont <= 10:
    
    aluno = float(input('digite a altura do aluno {}: '.format(cont)))

    cont += 1

    if aluno > maior:
        maior = aluno
        amostra1 = cont

    elif aluno < menor:
        menor = aluno
        amostra2 = cont

print('')
print('o aluno mais alto é o número {}, com {} m'.format(amostra1, maior))
print('o aluno mais baixo é o número {}, com {} m'.format(amostra2, menor))
