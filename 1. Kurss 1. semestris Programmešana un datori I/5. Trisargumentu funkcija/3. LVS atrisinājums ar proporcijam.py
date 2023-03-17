# Programmas nosaukums: 2.uzdevums ar proporciju salīdzināšanu metodi.
# 2. uzdevums (MPR5)
# Uzdevuma formulējums: Izveidot programmu, kas pieprasa ievadīt lineāras vienādojumu sistēmas koeficientu vērtības un paziņo tās atrisinājumu skaitu. Uzdevums jāatrisina, izmantojot determinantu metodi un ar koeficientu proporciju salīdzināšanas metodi.
# Programmas autors: Vladislavs Babaņins
# Versija 2.4

# Informācija lietotājam
print("2. kārtas lineāras vienādojumu sistēmas atrisinājums izmantojot proporciju salidzināšanu metodi\n\nax + by = c\ndx + ey = f\n")

# a,b,c,d,e,f vērtību input

a = float(input("Ievadiet a vērtību ===> "))
b = float(input("Ievadiet b vērtību ===> "))
c = float(input("Ievadiet c vērtību ===> "))
d = float(input("Ievadiet d vērtību ===> "))
e = float(input("Ievadiet e vērtību ===> "))
f = float(input("Ievadiet f vērtību ===> "))

# Determinantu apreķināšana (Lai paradītu atrisinājumu, ja tads ir)
D=a*e-b*d
Dx=c*e-b*f
Dy=a*f-c*d

# Gadījums, kad nav atrisinājums
if a/d == b/e and b/e != c/f:
    print("\n"+str(a)+"x + " + "(" + str(b) + ")"+ "y"+" = "+str(c))
    print(str(d)+"x + " + "(" + str(e) + ")"+ "y"+" = "+str(f))
    
    print("\nNav atrisinājumu")

# Gadījums, kad bezgalīgi daudz atrisinājumu  
if a/d==b/e and b/e==c/f :
    print("\n"+str(a)+"x + " + "(" + str(b) + ")"+ "y"+" = "+str(c))
    print(str(d)+"x + " + "(" + str(e) + ")"+ "y"+" = "+str(f))    
    
    print("\nBezgalīgi daudz atrisinājumu")

# Ir viens atrisinājums
if a/d != b/e:

    x=Dx/D
    y=Dy/D
    
    print("\n"+str(a)+"x + " + "(" + str(b) + ")"+ "y"+" = "+str(c))
    print(str(d)+"x + " + "(" + str(e) + ")"+ "y"+" = "+str(f))
    
    print("\nx = "+str(x)+"\ny = "+str(y))