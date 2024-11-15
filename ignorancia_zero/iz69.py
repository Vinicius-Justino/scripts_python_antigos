def multiplicaçao(*fatores):
    resultado = 1

    for contas in fatores:
        resultado *= contas

    return resultado

print(multiplicaçao(1, 2, 3, 4, 5))
