def maior(*argumentos):
    m = argumentos[0]

    for comparaçoes in argumentos:
        if comparaçoes > m:
            m = comparaçoes

    print(m)

maior(1, 2, 3, 4, 5)
maior(3, 1, 2, 5, 4)
maior(-1, -6, -3, 0)
