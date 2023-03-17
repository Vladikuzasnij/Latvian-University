# Programmas nosaukums: Piecsturis bez slidēšanas veļas x ass pozitīvajā virzienā...
# 5. uzdevums (MPR5)
# Uzdevuma formulējums: Dotais piecstūris bez slīdešanas veļas x ass pozitīvajā virzienā. Noteikt, kura izliekta piecstūra mala vai virsotne uzkritis uz punktu F. Punktu koordinātas ievada lietotājs.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0

import math

print("Izliekts piecsturis bez slidēšanas veļas x ass pozitīvajā virzienā.\nProgramma noteic kura izliekta piecstūra mala vai virsotne uzkritis uz punktu F.\nIevadiet koordinātas tikai 1.kvadrantā un tikai tādas koordinātas, lai veidotos izliekts piecstūris!\n")

x1 = float(input("Ievadiet x1 ===> ")) # A punkts

x2 = float(input("Ievadiet x2 ===> ")) # B punkts

x3 = float(input("Ievadiet x3 ===> ")) # C punkts
y3 = float(input("Ievadiet y3 ===> "))

x4 = float(input("Ievadiet x4 ===> ")) # D punkts
y4 = float(input("Ievadiet y4 ===> "))

y5 = float(input("Ievadiet y5 ===> ")) # E punkts

x6 = float(input("Ievadiet x6 ===> ")) # F punkts

# Katras malas garums

#AB mala

AB=x2-x1

#BC mala

BC=math.sqrt((x3-x2)*(x3-x2)+(y3*y3))

#DC mala

CD=math.sqrt((x3-x4)*(x3-x4)+(y4-y3)*(y4-y3))

#DE mala

DE=math.sqrt((y4-y5)*(y4-y5)+x4*x4)

#EA mala

EA=math.sqrt(y5*y5+x1*x1)

# ------------ #

#OA mala

OA=x1

#OF mala

OF=x6

# ------------ #

#Perimetrs

Perimeter= int(AB)+int(BC)+int(CD)+int(DE)+int(EA)
if OF<OA :
    print("Piecsturis nekad neuzkritīs uz punktu F") # Ka OF<OA tad piecsturis neuzkritīs uz punktu F, jo piecsturis veļas x ass pozitīvajā virzienā.
    
else:
    z=(OF-OA) # z - ceļš kuru piecsturim ir jāparverš
    u=math.floor(z/Perimeter) # u - cik reizes ceļš ietilpst piecstura perimetrā
    Atl=z-u*Perimeter # atl - atlikums
    AC=AB+BC # AC nogriežņa garums
    AD=AB+BC+CD # AD nogriežņa garums
    AE=AB+BC+CD+DE # AE nogriežņa garums
    
    if Atl==0:
        print("F atrodas uz punkta A")
    
    if Atl > 0 and Atl < AB: # Atrodas šajos robežos
        print("F atrodas uz AB nogriežņa")
        
    
    if Atl==AB:
        print("F atrodas uz punkta B")    
    
    if Atl > AB and Atl < AC :
        print("F atrodas uz BC nogriežņa")

        
    if Atl==AC :
        print("F atrodas uz punkta C")
        
    if Atl > AC and Atl < AD :
        print("F atrodas uz CD nogriežņa")
    
    
    if Atl==AD :
        print("F atrodas uz punkta D")
            
    if Atl > AD and Atl < AE :
        print("F atrodas uz DE nogriežņa")
        
    
    if Atl==AE :
        print("F atrodas uz punkta E")