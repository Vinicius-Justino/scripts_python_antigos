salas = int(input('digite o número de salas: '))
print('')
media = 0

for classes in range(1, salas+1):
    alunos = int(input('digite o número de alunos na sala {}: '.format(classes)))
    while alunos > 40 or alunos <= 0:
        print('')
        print('cada sala deve ter no mínimo 1 aluno, e pode ter no máximo 40 alunos.')
        alunos = int(input('digite o número de alunos na sala {}: '.format(classes)))
        
    media += alunos

print('')
print('a média da escola é de {:.1f} alunos por sala.'.format(media/salas))
if (media/salas)%1 != 0:
    print('ai meu deus, vocês cortam crianças no meio!')
