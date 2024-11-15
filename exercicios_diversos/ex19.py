#importaçâo
import random
#alunos
a1 = input('digite o nome do primeiro aluno(a):')
a2 = input('digite o nome do segundo aluno(a):')
a3 = input('digite o nome do terceiro aluno(a):')
a4 = input('digite o nome do quarto aluno(a):')
l = [a1, a2, a3, a4]
#sorteio
s1 = random.choice(l)
#resultado
print('entre os(as) alunos(as): {}, {}, {} e {},o sorteado foi {}.'.format(a1, a2, a3, a4, s1))
