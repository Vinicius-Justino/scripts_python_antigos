from random import choice

def criamatriz():
    opçoes = list(range(16))
    for linhas in range(4):
        linha = []
        for elementos in range(4):
            num = choice(opçoes)
            linha += [num]
            opçoes.remove(num)

        print(linha)

criamatriz()
