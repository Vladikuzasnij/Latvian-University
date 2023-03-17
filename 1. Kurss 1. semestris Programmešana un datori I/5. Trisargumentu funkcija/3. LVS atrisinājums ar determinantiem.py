# Programmas nosaukums: 2.uzdevums ar determinanta metodi.
# 2. uzdevums (MPR5)
# Uzdevuma formulējums: Izveidot programmu, kas pieprasa ievadīt lineāras vienādojumu sistēmas koeficientu vērtības un paziņo tās atrisinājumu skaitu. Uzdevums jāatrisina, izmantojot determinantu metodi un ar koeficientu proporciju salīdzināšanas metodi.
# Programmas autors: Vladislavs Babaņins
# Versija 4.6


# Informācija lietotājam
print("2. kārtas lineāras vienādojumu sistēmas atrisinājums izmantojot Krāmera formulas\n\nax + by = c\ndx + ey = f\n")

# a,b,c,d,e,f vērtību input

a = float(input("Ievadiet a vērtību ===> "))
b = float(input("Ievadiet b vērtību ===> "))
c = float(input("Ievadiet c vērtību ===> "))
d = float(input("Ievadiet d vērtību ===> "))
e = float(input("Ievadiet e vērtību ===> "))
f = float(input("Ievadiet f vērtību ===> "))

# Determinantu apreķināšana
D=a*e-b*d
Dx=c*e-b*f
Dy=a*f-c*d

# Ja Sistēmas determinants ir 0 un (Dx != 0 vai Dy != 0 tad nav atrisinājumu)

if D==0 and (Dx !=0 or Dy !=0) :
    print("\n"+str(a)+"x + " + "(" + str(b) + ")"+ "y"+" = "+str(c))
    print(str(d)+"x + " + "(" + str(e) + ")"+ "y"+" = "+str(f))
    
    print("\nNav atrisinājumu")

# Ja visi determinanti (D == 0 un Dx == 0 un Dy == 0) tad ir bezgalīgi daudz atrisinājumu

if D==0 and Dx == 0 and Dy==0 :
    print("\n"+str(a)+"x + " + "(" + str(b) + ")"+ "y"+" = "+str(c))
    print(str(d)+"x + " + "(" + str(e) + ")"+ "y"+" = "+str(f))    
    
    print("\nBezgalīgi daudz atrisinājumu")

# Ja sistēmas determinants nav 0, tad ir viens vienīgs atrisinājums
    
if D!=0:

    x=Dx/D
    y=Dy/D
    
    print("\n"+str(a)+"x + " + "(" + str(b) + ")"+ "y"+" = "+str(c))
    print(str(d)+"x + " + "(" + str(e) + ")"+ "y"+" = "+str(f))
    
    print("\nx = "+str(x)+"\ny = "+str(y))