def TiraEspaços():
    '''
Remove os espaços em branco de uma expressão, para não causarem problemas
no futuro.
    '''
    global conta

    aux = list(conta)
    
    for remove_espaços in aux:
        if remove_espaços == ' ':
            aux.remove(remove_espaços)

    conta = ''
    for remonta_conta in aux:
        conta += remonta_conta


def ProcuraParenteses(conta):
    '''
Procura contas entre parênteses na expressão para fazê-las primeiro.
    '''
    for procura in range(len(conta)):
        if conta[procura] == '(':
            abriu = procura

        elif conta[procura] == ')':
            fechou = procura+1
            break

    try:
        return [abriu, fechou]
    except NameError:
        return [0, len(conta)-1]


def EncontraNumero1(conta, local):
    '''
Encontra o número que está à esquerda de um sinal.
    '''
    numero = ''
    algarismos = []
    algarismo = local-1

    while '0' <= conta[algarismo] <= '9' and algarismo >= 0:
        algarismos += conta[algarismo]
        algarismo -= 1

    algarismos.reverse()
    for monta_numero in algarismos:
        numero += monta_numero

    return int(numero)


def EncontraNumero2(conta, local):
    '''
Encontra o número que está à direita de um sinal.
    '''
    numero = ''
    algarismo = local+1

    while algarismo < len(conta):
        if '0' <= conta[algarismo] <= '9':
            numero += conta[algarismo]
            algarismo += 1

        else:
            break

    return int(numero)


def EfetuaOperaçao(referencia, numero1, numero2, resultado):
    '''
Efetua uma operação e coloca o resultado obtido no seu lugar na expressão.
    '''
    global conta
    
    aux = list(conta)

    tirou1 = ''
    tirou2 = ''

    #print("\n\nConta:", aux)
    for Remove_numero1 in range(len(str(numero1))):
        tirou1 += aux[referencia-1]
        tira = aux.pop(referencia-1)
        referencia -= 1
    #print("\nTirou:", tirou1)

    #print("Ficou:", aux)
    for Remove_numero1 in range(len(str(numero2))):
        tirou2 += aux[referencia+1]
        tira = aux.pop(referencia+1)
    #print("Tirou mais:", tirou2)

    aux[referencia] = str(round(resultado))
    #print("Ficou:", aux)

    conta = ''
    for monta_conta in aux:
        conta += monta_conta


def ResolveOperaçoes():
    '''
Procura por operações em uma expressão e as efetua.
    '''
    global parenteses, conta

    foi_feita_uma_operaçao = False
    
    for prioridade in range(1, 4):
        if foi_feita_uma_operaçao:
            break
        
        for sinal in range(parenteses[0], parenteses[1]):
            if prioridade == 1:
                if conta[sinal] == '^':
                    n1 = EncontraNumero1(conta, sinal)
                    n2 = EncontraNumero2(conta, sinal)
                    EfetuaOperaçao(sinal, n1, n2, n1**n2)
                    foi_feita_uma_operaçao = True
                    

                elif conta[sinal] == 'r':
                    n1 = EncontraNumero1(conta, sinal)
                    n2 = EncontraNumero2(conta, sinal)
                    EfetuaOperaçao(sinal, n1, n2, n1**(1/n2))
                    foi_feita_uma_operaçao = True

            elif prioridade == 2:
                if conta[sinal] == 'x':
                    n1 = EncontraNumero1(conta, sinal)
                    n2 = EncontraNumero2(conta, sinal)
                    EfetuaOperaçao(sinal, n1, n2, n1*n2)
                    foi_feita_uma_operaçao = True

                elif conta[sinal] == '/':
                    n1 = EncontraNumero1(conta, sinal)
                    n2 = EncontraNumero2(conta, sinal)
                    EfetuaOperaçao(sinal, n1, n2, n1//n2)
                    foi_feita_uma_operaçao = True

            elif prioridade == 3:
                if conta[sinal] == '+':
                    n1 = EncontraNumero1(conta, sinal)
                    n2 = EncontraNumero2(conta, sinal)
                    EfetuaOperaçao(sinal, n1, n2, n1+n2)
                    foi_feita_uma_operaçao = True

                elif conta[sinal] == '-':
                    operaçao = sinal
                    n1 = EncontraNumero1(conta, sinal)
                    n2 = EncontraNumero2(conta, sinal)
                    EfetuaOperaçao(sinal, n1, n2, max(n1, n2)-min(n1, n2))
                    foi_feita_uma_operaçao = True 

            parenteses = ProcuraParenteses(conta)
            if not parenteses == [0, len(conta)-1]:
                if not TemContaPraFazer(conta[parenteses[0]:parenteses[1]]):
                    try:
                        aux = list(conta)
                        tira = aux.pop(parenteses[1]-1)
                        tira = aux.pop(parenteses[0])

                        conta = ''
                        for remonta_conta in aux:
                            conta += remonta_conta
                    except:
                        None

            if foi_feita_uma_operaçao:
                break


def TemContaPraFazer(conta):
    '''
Verifica se ainda tem contas para fazer na expressão.
    '''
    for confere in conta:
        if confere == '+' or confere == '-' or confere == 'x' or confere == '/' or confere == '^' or confere == 'r':
            return True
        
    return False

#==============================================================================#
                    
print(" "*22 + "Calculadora de expressões numéricas!" + " "*22)
print("\n- Use apenas parênteses para priorizar contas.")
print("- Use + para somar dois números. Tipo 2+2")
print("- Use - para subtrair. Tipo 70-1")
print("- Use x para multiplicar. Tipo 3x3")
print("- Use / para dividir. Tipo 10/2")
print("- Use ^ para fazer potências. Tipo 2^2")
print("- Use r depois de um número para ver a sua raiz. Tipo 25r2 (raiz quadrada) ou \n  64r3 (raiz cúbica).")
print("- Use apenas números naturais.")
print("- Subtrações sempre serão feitas como maior-menor.")
print("- As divisões serão feitas sem parte decimal.")

while True:
    try:
        conta = input("\n> ")
        TiraEspaços()
        
        while TemContaPraFazer(conta):
            parenteses = ProcuraParenteses(conta)
            ResolveOperaçoes()
            print(">",conta)
    except:
        print("> Ops! Parece que aconteceu erro ao tentarmos resolver a sua expressão, leia \n  todas as regras desse programa com calma e depois revize sua conta, por \n  gentileza.")
