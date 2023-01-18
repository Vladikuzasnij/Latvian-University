# Programmas nosaukums: Funkcijas vērtību aprēķins
# 1. uzdevums (MPR5)
# Uzdevuma formulējums: Izveidot programmu, kura pēc funkcijas ievadītās argumenta x vērtības aprēķina tās vērtību.
# Programmas autors: Vladislavs Babaņins
# Versija 1.1

import math # Lai izmantotu mat.log funkciju

x = float(input("Ievadiet argumenta x vērtību ===> ")) # Paprasīt lietotājam ievadit x vērtību

if x<3 and x>-3 : # Ja x atrodas tādas robežas tad :
    a=(x+3)*(x+3)
    print("x = " + str(x) + " \nf(x) = "+ (str(a))) # Izvada ekrāna vērtības
    
if  x<-10 or x>10: # Ja x atrodas tādas robežas tad :
    a=math.log((x*x),2)
    print("x = " + str(x) + " \nf(x) = "+ (str(a)))

if  (x >= 3 and x <= 10) or (x <= -3 and x>=-10): # Ja x atrodas tādas robežas tad :
    a=81-x*x
    print("x = " + str(x) + " \nf(x) = "+ (str(a)))