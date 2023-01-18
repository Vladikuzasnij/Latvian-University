# Programmas nosaukums: 5. uzd MPR10
# 5. uzdevums MPR10
# Uzdevuma formulējums: Sastādīt programmu, kas nodrukā visus laimīgos loterijas biļešu numurus.
# Ja zināms, ka loterijas biļešu numuri ir četrciparu skaitļi no 0000 līdz 9999, bet par laimīgiem tie uzskatīti
# tie numuri, kas apmierina šādus nosacījumus:
# 1) visi cipari ir dažādi.
# 2) Pirmo divu un pēdējo divu ciparu veidoto skaitļu summa ir vienāda ar visu četru ciparu reizinājumu.
# Versija 1.0

for a in range(0, 10) :
    for b in range(0, 10) :
        for c in range(0, 10) :
            for d in range(0, 10) :

                if ((a!=0) and (b!=0) and
                    (c!=0) and (d!=0) and
                    (a!=b) and (a!=c) and
                    (a!=d) and (b!=c) and
                    (b!=d) and (c!=d) and
                    (10*a+b+10*c+d==a*b*c*d)) :
                    print (str(a) + str(b) +
                           str(c) + str(d))