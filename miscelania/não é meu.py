area = int(input("Qual a área a ser pintada? "))
litros = (area / 6)
litrost = litros + (litros/100*10)
tinta1 = 18
tinta2 = 4
p1 = 80
p2 = 25
lata1 = litrost/tinta1
lata2 = litrost/tinta2
lata3 = litrost//tinta1
_lata = litrost % tinta1
lata4 = _lata / tinta2 
lataint4 = _lata // tinta2
lataint1 = litrost//tinta1
lataint2 = litrost//tinta2
pt3 = (lata3 * p1 + lata4 * p2)

if lata4 < 1:
    lata4 = 1
    pt3 = (lata3 * p1 + lata4 * p2)
elif lata4 != lataint4:
    lata4 = lataint4
    pt3 = (lata3 * p1) + ((lata4+1) * p2)
else:
    pt3 = (lata3 * p1) + ((lata4) * p2)

if lata1<1:
    lata1 = 1 
    pt1 = lata1 * p1
elif lata1 != lataint1:
    lata1 = lataint1 + 1
    pt1 = lata1 * p1
else:
    pt1 = lata1 * p1

if lata1<1:
    lata2 = 1 
    pt2 = lata2 * p2
elif lata2 != lataint2:
    lata2 = lataint2 + 1
    pt2 = lata2 * p2
else:
    pt2 = lata2 * p2


print("Você precisará de",litrost,"litros de tinta")
if lata1 == 1:
    print("você precisará de",lata1,"lata de tinta de",tinta1,"litros, custando",p1,"reais. Dando no total",pt1,"reais")
else:
    print("você precisará de",lata1,"latas de tinta de",tinta1,"litros, custando",p1,"reais. Dando no total",pt1,"reais")
print("ou")
if lata2 == 1:
    print("você precisará de",lata2,"galões de",tinta2,"litros, custando",p2,"reais. Dando no total",pt2,"reais")
else:
    print("você precisará de",lata2,"galões de",tinta2,"litros, custando",p2,"reais. Dando no total",pt2,"reais")
print("ou")
print("você precisará de",lata3,"latas de tinta de",tinta1,"litros, custando",p1,"reais e",lata4,"galões de",tinta2,"litros, custando",p2,"reais.Dando no total",pt3,"reais")

