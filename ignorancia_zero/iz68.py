def nota(notas, peso):
    media = 0
    pesos = 0
    for valores in range(len(notas)):
        media += notas[valores] * peso[valores]
        pesos += peso[valores]

    media /= pesos

    return media

print(nota((5, 5, 5), (1, 1, 1)))
