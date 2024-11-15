#COLHENDO OS DADOS DO PRIMEIRO ARQUIVO
usuarios = open('usuários.txt')
aux_usuarios1 = open('usuários.txt')
aux_usuarios2 = open('usuários.txt')

def converte(tamanho):
    return float('{:.2f}'.format(tamanho/1000000))

nomes = []
tamanhos = []
aux_tamanhos = []
total = 0

for arruma in range(len(aux_usuarios1.readlines())):
    nome = ''
    tamanho = ''
    
    aux = usuarios.readline()

    for separa in aux:
        if '1' <= separa <= '9':
            tamanho += separa

        if 'a' <= separa <= 'z' or 'A' <= separa <= 'Z':
            nome += separa

        if separa == '\\':
            break

    tamanho = converte(int(tamanho))

    if nome != '' and tamanho != 0:
        tamanhos += [tamanho]
        total += tamanho
        aux_tamanhos += [tamanho]
        nomes += [nome]

usuarios.close()

#ARRUMANDO NO SEGUNDO ARQUIVO
relatorio = open('relatório.txt', 'w')

aux_tamanhos.sort()
aux_nomes = []

def porcento(total, parcela):
    return float('{:.2f}'.format((parcela*100)/total))

for classi in range(len(tamanhos)):
    aux_nomes += [nomes[tamanhos.index(aux_tamanhos[classi])]]

nomes = aux_nomes
tamanhos = aux_tamanhos

nomes.reverse()
tamanhos.reverse()

relatorio.write('ACME Inc.                   Uso do espaço em disco pelos usuários \n')
relatorio.write('---------------------------------------------------------------------------- \n')
relatorio.write('nº     Usuário              Espaço utilizado             % do uso \n')
relatorio.write('\n')
for mostra in range(1, len(aux_usuarios2.readlines())+1):
    saida = str(mostra) + 'º' + ' '*5
    saida += nomes[mostra-1] + ' '*(14 - len(nomes[mostra-1]))
    saida += ' '*(15 - len(str(tamanhos[mostra-1]))) + str(tamanhos[mostra-1]) + ' MB'
    saida += ' '*(24 - len(str(porcento(total, tamanhos[mostra-1])))) + str(porcento(total, tamanhos[mostra-1])) + '%'

    relatorio.write('{} \n'.format(saida))

relatorio.write('Espaço total ocupado: {:.2f} \n'.format(total))
relatorio.write('Média por usuário: {:.2f}'.format(total/len(tamanhos)))

relatorio.close()
