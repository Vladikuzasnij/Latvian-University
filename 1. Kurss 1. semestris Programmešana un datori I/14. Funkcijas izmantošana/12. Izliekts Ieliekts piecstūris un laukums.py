# Programmas nosaukums: 3. uzd MPR14
# 3. uzdevums MPR14
# Uzdevuma formulējums: Sastādīt programmu, kas nosaka, vai dotais piecstūris ir vai nav izliekts. Ja piecstūris ir izliekts, tā aprēķina tā laukumu. Piecstūra virsotņu koordinātas secīgi pulksteņa rādītajā virzienā ievada lietotājs.
# Versija 1.0

import math

def line_and_check(x1,y1,x3,y3,x2,y2,x4,y4):
    a = y3-y1
    b = x1-x3
    c = x3*y1-x1*y3

    z1=a*x2+b*y2+c
    z3=a*x4+b*y4+c
    
    if (z1*z3>0) :
        return False
        #print("Punkti ir vienā pusē taisnei.")    
    else :
        return True
        #print("Punkti nav vienā pusē taisnei.")

# x*(y3-y1)+y*(x1-x3)+x3*y1-x1*y3=0

print("Programma nosaka, vai dotais piecstūris ir vai nav izliekts.\nJa piecstūris ir izliekts, tā aprēķina tā laukumu.\nPiecstūra virsotņu koordinātas secīgi pulksteņa rādītajā virzienā ievada lietotājs.\n")
x1 = input("Ievadi x1 ===> ")
y1 = input("Ievadi y1 ===> ")

x2 = input("Ievadi x2 ===> ")
y2 = input("Ievadi y2 ===> ")

x3 = input("Ievadi x3 ===> ")
y3 = input("Ievadi y3 ===> ")

x4 = input("Ievadi x4 ===> ")
y4 = input("Ievadi y4 ===> ")

x5 = input("Ievadi x5 ===> ")
y5 = input("Ievadi y5 ===> ")

M=1
while M<3:
    try:
        x1 = float(x1)
        y1 = float(y1)
        
        x2 = float(x2)
        y2 = float(y2)
        
        x3 = float(x3)
        y3 = float(y3)
        
        x4 = float(x4)
        y4 = float(y4)
        
        x5 = float(x5)
        y5 = float(y5)
        
    except:
        M=M+1
        print("\nKaut viena koordināta tika nekorekti ievadīta. Ievadiet realus skaitļus!\n")
        x1 = input("Ievadi x1 ===> ")
        y1 = input("Ievadi y1 ===> ")

        x2 = input("Ievadi x2 ===> ")
        y2 = input("Ievadi y2 ===> ")

        x3 = input("Ievadi x3 ===> ")
        y3 = input("Ievadi y3 ===> ")

        x4 = input("Ievadi x4 ===> ")
        y4 = input("Ievadi y4 ===> ")

        x5 = input("Ievadi x5 ===> ")
        y5 = input("Ievadi y5 ===> ")

    else:

        if ((line_and_check(x1,y1,x3,y3,x2,y2,x4,y4)) and line_and_check(x1,y1,x3,y3,x2,y2,x5,y5) and
             line_and_check(x1,y1,x4,y4,x2,y2,x5,y5) and line_and_check(x1,y1,x4,y4,x3,y3,x5,y5) and
             line_and_check(x2,y2,x4,y4,x3,y3,x1,y1) and line_and_check(x2,y2,x4,y4,x3,y3,x5,y5) and
             line_and_check(x2,y2,x5,y5,x1,y1,x3,y3) and line_and_check(x2,y2,x5,y5,x1,y1,x4,y4) and
             line_and_check(x3,y3,x5,y5,x4,y4,x2,y2) and line_and_check(x3,y3,x5,y5,x4,y4,x1,y1) and 
             line_and_check(x3,y3,x1,y1,x2,y2,x5,y5) and line_and_check(x3,y3,x1,y1,x2,y2,x4,y4) and
             line_and_check(x4,y4,x2,y2,x1,y1,x3,y3) and line_and_check(x4,y4,x2,y2,x5,y5,x3,y3) and
             line_and_check(x5,y5,x2,y2,x1,y1,x3,y3) and line_and_check(x5,y5,x2,y2,x1,y1,x4,y4)):
            
            print("\nPiecstūris ir izliekts")
            S1 = 0.5*((x2-x1)*(y3-y1)-(x3-x1)*(y2-y1))
            S2 = 0.5*((x3-x1)*(y5-y1)-(x5-x1)*(y3-y1))
            S3 = 0.5*((x3-x5)*(y4-y5)-(x4-x5)*(y3-y5))
            S = S1 + S2 + S3
            print("S = " + str(abs(S)))
            quit()

        else:
            print("\nPiecstūris ir ieliekts. Programma nevar aprēķināt ieliekta piecstūra laukumu.")
            quit()
            
print("\nJūs 3 reizes kļūdījāties. Beidzam sadarbību!")