# Programmas nosaukums: 5.uzdevums (PU)
# 5.uzdevums MPR7 PU (ar visiem izņemumiem)
# Uzdevuma formulējums: Izveidot programmu, kas jebkuru lietotāja ievadīto trīsciparu skaitli Romiešu pierakstā konvertē un izvada uz ekrāna Arābu pierakstā.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0

import sys

print("Pieejamie simboli:\nI - 1 \nV - 5 \nX - 10 \nL - 50 \nC - 100 \nD - 500 \nM - 1000\n")

A = str(input("Ievadiet pirmo Romiešu ciparu skaitļa pieraksta (pirmo simbolu)\n===> "))
B = str(input("Ievadiet otro Romiešu ciparu skaitļa pieraksta (otro simbolu)\n===> "))
C = str(input("Ievadiet trešo Romiešu ciparu skaitļa pieraksta (trešo simbolu)\n===> "))

if A+B+C == "VVV" or A+B+C == "LLL" or A+B+C == "DDD":
    print("Neder")
    sys.exit(0)

match A :
    case "I" :
        A = 1
    case "V" :
        A = 5
    case "X" :
        A = 10
    case "L" :
        A = 50
    case "C" :
        A = 100
    case "D" :
        A = 500
    case "M" :
        A = 1000
    case other :
        print("Error")
        sys.exit(0)        
    
    
match B :
    case "I" :
        B = 1
    case "V" :
        B = 5
    case "X" :
        B = 10
    case "L" :
        B = 50
    case "C" :
        B = 100
    case "D" :
        B = 500
    case "M" :
        B = 1000
    case other :
        print("Error")
        sys.exit(0)
        
match C :
    case "I" :
        C = 1
    case "V" :
        C = 5
    case "X" :
        C = 10
    case "L" :
        C = 50
    case "C" :
        C = 100
    case "D" :
        C = 500
    case "M" :
        C = 1000
    case other :
        print("Error")
        sys.exit(0)
       
if A >= B:
    if B >= C:
        
        if (B == 5 and C == 5) or (B == 50 and C == 50) or (B == 500 and C == 500):
            print("Neder")
            sys.exit(0)
         
        else:
            #print("A + B + C")
            print(A+B+C)
            sys.exit(0)
        
        
    elif A>=C:
        
        if B == 10 and (C == 50 or C == 100):
            print(A+C-B)
            sys.exit(0)
            
        if B == 100 and (C == 500 or C == 1000):
            print(A+C-B)
            sys.exit(0)        
            
        if A != 10 and A == C:
            print("Neder")
            sys.exit(0)
            
        if B == 5 and C == 10:
            print("Neder")
            sys.exit(0)
        
        if B != 1 or B != 5 and C >= 50:
            print("Neder")
            sys.exit(0)
            
        if B == 1 and C == 5 or C == 10:
            print(A+C-B)
            sys.exit(0)
            
        else:
            #print("A + C - B")
            print(A+C-B)
            sys.exit(0)
    
    else:
        print("Neder")
        sys.exit(0)


elif B <= C:
    print("Neder")
    sys.exit(0)
    
    
elif A <= C:
    print("Neder")
    sys.exit(0)
    
    
else:
    if A > C:
        print("Neder")
        sys.exit(0)
        
        
    else:
        #print("-A + B + C")
        print(B+C-A)
        sys.exit(0)

