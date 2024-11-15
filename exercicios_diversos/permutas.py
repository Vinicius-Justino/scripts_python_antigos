from sys import argv
from os import remove

with open("auxiliar.py", "w") as aux:
    comprimento = int(argv[1])
    caracteres = [i for i in argv[2] if i.isalnum()]

    aux.write(f"caracteres = {caracteres} \n")
    aux.write("permuta = [{} \" \"] \n\n".format('\" \",' * (comprimento - 1)))

    for i in range(1, comprimento + 1):
        aux.write("{}for c{} in range({}): \n".format('\t' * (i - 1), i, len(caracteres)))
        aux.write("{}permuta[{}] = caracteres[c{}] \n".format('\t' * i, i - 1, i))

    aux.write("{}string_permuta = '' \n".format('\t' * comprimento))
    aux.write("{}for i in permuta: string_permuta += i \n".format('\t' * comprimento))
    aux.write("{}print(string_permuta) \n".format('\t' * comprimento))

import auxiliar
remove("auxiliar.py")
