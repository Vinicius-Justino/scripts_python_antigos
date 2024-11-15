def somaMultiplos(numero, limite):
    # Calcula a soma apenas se as entradas forem válidas
    if not limite or not numero:
        return 0

    # desconsideramos o resto de limite / numero
    limite -= limite % numero

    # Soma todos os múltiplos de numero entre 0 e limite 
    soma = 0
    for multiplo in range(numero, limite + 1, numero):
        soma += multiplo

    return soma

print(somaMultiplos(3, 49) + somaMultiplos(5, 49))
