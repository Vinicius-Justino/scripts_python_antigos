def replace(string, velha, nova):
    saida = string

    for novo in range(len(string)+1 - len(velha)):
        if string[novo:novo+len(velha)] == velha:
            saida = saida[:saida.find(velha)] + nova + saida[(saida.find(velha)+2):]

    return saida

print(replace('mississipi', 'ss', 'c'))
