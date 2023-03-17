# Programmas nosaukums: Sakartot trīs skaitļus dilstoša secība
# 4. uzdevums (MPR4)
# Uzdevuma formulējums: Izveidot programmu, kura pieprasa ievadīt trīs skaitļus, sakārto un nodrukā tos dilstoša secība.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0

print("\"Sakartot trīs skaitļus dilstoša secība\"\nVersija 1.0\n")


a = float(input("Ievadiet 1.skaitli ===> "))
b = float(input("Ievadiet 2.skaitli ===> "))
c = float(input("Ievadiet 3.skaitli ===> "))

if a < b :
    p = a
    a = b
    b = p

if a < c :
    p = c
    c = a
    a = p

if b < c :
    p = b
    b = c
    c = p

print(str(a), str(b), str(c))