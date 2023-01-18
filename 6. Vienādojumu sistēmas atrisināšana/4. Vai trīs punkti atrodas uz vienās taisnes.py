# Programmas nosaukums: 3.uzdevums
# 3.uzdevums MPR6
# Uzdevuma formulējums: Izveidot programmu, kas, pēc lietotāja ievadītajām trīs punktu A(x1, y1), B(x2, y2) un C(x3, y3) koordinātām, noskaidro un paziņo, vai šie trīs punkti atrodas uz vienas taisnes.
# Programmas autors: Vladislavs Babaņins
# Versija 2.3

x1 = float(input("Ievadiet x1 ===> "))
y1 = float(input("Ievadiet y1 ===> "))

x2 = float(input("Ievadiet x2 ===> "))
y2 = float(input("Ievadiet y2 ===> "))

x = float(input("Ievadiet x3 ===> "))
y = float(input("Ievadiet y3 ===> "))


a=(x-x2)*(y1-y2)
b=(y-y2)*(x1-x2)

if a==b:
    print("\nPunkti atrodas uz vienas taisnes")
    
if a!=b:
    print("\nPunkti nav uz vienas taisnes")