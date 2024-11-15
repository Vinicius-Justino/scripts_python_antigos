#importação
import random
#alunos
a1 = input('digite o nome do primeiro aluno:')
a2 = input('digite o nome do segundo aluno:')
a3 = input('digite o nome do terceiro aluno:')
a4 = input('digite o nome do quarto aluno:')
l = [a1, a2, a3, a4]
#sorteio
o = random.shuffle(l)
#resultado
print('a ordem de apresentação será: {}'.format(o))
