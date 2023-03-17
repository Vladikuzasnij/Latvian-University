# Programmas nosaukums: Trījstura paramētri
# 3. uzdevums
# Uzdevuma formulējums: Izveidot programmu, kura pēc visu trijstūra malu ievades, paziņo tā: perimetru, laukumu, ap to apvilktās riņķa līnijas rādiusu, tajā ievilktās riņķa līniju rādiusu.
# Programmas autors: Vladislavs Babaņins
# Versija 2.2

import math

print("\"Trījstura paramētri\"\nVersija 2.2\n")

a=float(input("Ievadi 1. mālu ===>"))
b=float(input("Ievadi 2. mālu ===>"))
c=float(input("Ievadi 3. mālu ===>"))

# Trījstura nevienādības pārbaudīšana

if   a >= b+c:
    print("Tāds trījsturis neēksiste")
elif b >= a+c:
    print("Tāds trījsturis neēksiste")
elif c >= a+b:
    print("Tāds trījsturis neēksiste")
else:
    
    perimeter=(a+b+c) # Perimetra apreķināšana
    print("Trijstūra perimetrs: "+str(perimeter))

    p=(a+b+c)/2 # Pusperimetra apreķināšana

    area=math.sqrt(p*(p-a)*(p-b)*(p-c)) # Laukuma apreķināšana izmantojot Herona formulu
    print("Laukums: "+str(area))
    
    R=(a*math.sqrt(3)/3) # Apvilktas riņķa līnijas rādiuss
    print("Apvikltas riņķa līnijas rādiuss: "+str(R))
    
    r=(a*math.sqrt(3)/6) # Ievilktas riņķa līnijas rādiuss
    print("Ievilktas riņķa līnijas rādiuss: "+str(r))