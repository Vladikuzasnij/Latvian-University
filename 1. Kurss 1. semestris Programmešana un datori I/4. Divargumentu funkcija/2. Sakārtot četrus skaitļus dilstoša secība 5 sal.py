# Programmas nosaukums: Sakārtot četrus skaitļus dilstoša secība
# 6. uzdevums (MPR4)
# Uzdevuma formulējums: Izveidot programmu, kura pieprasa ievadīt četrus skaitļus, sakārto un nodrukā tos dilstoša secībā, izmantojot ne vairāk kā piecas salīdzināšanas darbības.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0

a = float(input("Ievadiet 1.skaitli ===> "))
b = float(input("Ievadiet 2.skaitli ===> "))
c = float(input("Ievadiet 3.skaitli ===> "))
d = float(input("Ievadiet 4.skaitli ===> "))

if a < b :
    x = a
    a = b
    b = x
    
if c < d :
    x = c
    c = d
    d = x

if a < c :
    x = c
    c = a
    a = x
    
if b < d :
    x = b
    b = d
    d = x
    
if b < c :
    x = b
    b = c
    c = x
    
print(str(a), str(b), str(c), str(d))