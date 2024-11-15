mensagem = """
VAMOS MORREEEER, VAMOS MORREERRRR, ELE.E_STA_.CHEGAAAANDOOOOOOOO, D.E_.US, DA MO.RTEE, E_LE.ME.PEGOUUUUUUU, ASSA.SSI.NO, D_EUUU_S DA_MORTEEEEEE, OC.ULTISTAAAAS_ , AS_ P.ON.TASS SOLTAAS., O. SOM_, DO_ INFERNOOO., O_ SOM. DO FIMMM., A_LGUÉM _ME AJUDA _, ELE _ VAI ME PEGAR., ESCURO. E VAZIOOOO _, É TÃO _ GRA.NDEEE., ELE _ ESTÁ _ CHEGANDO _

AS_PE.QUENAS_LI.NHAS SEPARAM.O.POEMA_ DA VIDA_
"""

morse = ""
for char in mensagem:
    if char == "." or char == "_":
        morse += char
    elif char == ",":
        morse += " "

print(morse)
input("")