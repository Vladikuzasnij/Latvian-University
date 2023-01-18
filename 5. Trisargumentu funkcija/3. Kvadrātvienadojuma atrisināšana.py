# Programmas nosaukums: Kvadrātvienādojuma atrisināšana
# 3. uzdevums (MPR5)
# Uzdevuma formulējums: Izveidot programmu, kas pieprasa ievadīt kvadrātvienādojuma koeficientus un paziņo tā saknes (reālo un komplekso skaitļu kopā).
# Programmas autors: Vladislavs Babaņins
# Versija 2.4

import math # Lai izmantotu math.sqrt()

print("Kvadrātvienādojumu atrisināšana")

a = float(input("Ievadiet a koeficientu ===> ")) # Input no lietotāja
b = float(input("Ievadiet b koeficientu ===> "))
c = float(input("Ievadiet c koeficientu ===> "))

# Nav kvadrātvienādojums pēc definīcijas
if a == 0 :
    
    print("\n("+str(a)+")*x^2 + " + "(" + str(b) + ")"+ "*x"+" + ("+str(c)+") = 0")
    print("\nTas nav kvadraatvienādojums")

else : # Citādi risinām kvadrātvienādojumu
    
    d = b*b - 4*a*c # Diskriminants

    if d < 0 : # Tad ir komplēksa skaitļi
        
        print("\n("+str(a)+")*x^2 + " + "(" + str(b) + ")"+ "*x"+" + ("+str(c)+") = 0")
        print("\nKvadrātvienādojumam realu saknu nav\nIr divas kompleksas saknes\n")
        
        Re = -b
        Im = abs(math.sqrt(-d) / (2 * a))
        print(f"x1 = {Re} + i*{Im} \nx2 = {Re} - i*{Im}")        

    elif d == 0 : # Tad divas vienādas saknes
        
        x12 = -b / 2 / a
        
        print("\n("+str(a)+")*x^2 + " + "(" + str(b) + ")"+ "*x"+" + ("+str(c)+") = 0")
        print("\nKvadrātvienādojumam ir divas vienādas saknes")
        print("x1 = x2 = " + str(x12))

    else : # Divas atšķirīgas saknes
        
        x1 = (-b + math.sqrt(d)) / 2 /a
        x2 = (-b - math.sqrt(d)) / 2 / a
        
        print("\n("+str(a)+")*x^2 + " + "(" + str(b) + ")"+ "*x"+" + ("+str(c)+") = 0")
        print("\nKvadrātvienādojumam ir divas atšķirīgas saknes")
        print("\nx1 = " + str(x1))
        print("x2 = " + str(x2))
    
