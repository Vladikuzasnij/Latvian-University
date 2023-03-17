# Programmas nosaukums: Bikvadrātvienādojuma atrisināšana
# 4. uzdevums (MPR5)
# Uzdevuma formulējums: Izveidot programmu, kas pieprasa ievadīt bikvadrātvienādojuma koeficientus un paziņo tā saknes reālo kopā. Uzzīmēt uzdevuma atrisināšanas blokshēmu.
# Programmas autors: Vladislavs Babaņins
# Versija 4.0

import math # Lai izmantotu math.sqrt()

print("Bikvadrātvienādojumu atrisināšana")

a = float(input("Ievadiet a koeficientu ===> "))
b = float(input("Ievadiet b koeficientu ===> "))
c = float(input("Ievadiet c koeficientu ===> "))

if a == 0 : # Pēc def. tas nav bikvadrātvienādojums ja a == 0
    
    print("\n("+str(a)+")*x^4 + " + "(" + str(b) + ")"+ "*x^2"+" + ("+str(c)+") = 0")
    print("\nTas nav bikvadrātvienādojums")

else :
    
    d = b*b - 4*a*c # Diskriminants

    if d < 0 : # Risinām ax^4 + bx^2+c=0. x^2 = t , at^2 + bt + c = 0, atrādam t1,t2 un tad atradam x1,x2 x = +-sqrt(t)
        
        print("\n("+str(a)+")*x^4 + " + "(" + str(b) + ")"+ "*x^2"+" + ("+str(c)+") = 0\n")
        print("\nBikvadrātvienādojumam nav reālas saknes")

        
    else :
        
        t1 = (-b + math.sqrt(d)) / 2 / a
        t2 = (-b - math.sqrt(d)) / 2 / a
        
        if t1 >= 0 :
            if t2 >=0:
                x1=math.sqrt(t1)
                x2=-1*(math.sqrt(t1))
                x3=math.sqrt(t2)
                x4=-1*(math.sqrt(t2))
                print("\n("+str(a)+")*x^4 + " + "(" + str(b) + ")"+ "*x^2"+" + ("+str(c)+") = 0\n")

                print("x1 = "+str(x1))
                print("x2 = "+str(x2))
                print("x3 = "+str(x3))
                print("x4 = "+str(x4))                
            
            else:
                
                x1= math.sqrt(t1)
                x2 = -1*(math.sqrt(t1))
                print("\n("+str(a)+")*x^4 + " + "(" + str(b) + ")"+ "*x^2"+" + ("+str(c)+") = 0\n")
                
                print("x1 = "+str(x1))
                print("x2 = "+str(x2))
                
            
        elif t2>=0:
            x1 = math.sqrt(t2)
            x2 = -1*(math.sqrt(t2))
            print("\n("+str(a)+")*x^4 + " + "(" + str(b) + ")"+ "*x^2"+" + ("+str(c)+") = 0\n")
            print("x1 = "+str(x1))
            print("x2 = "+str(x2))
            
        else:
            print("Sakņu nav")

    
