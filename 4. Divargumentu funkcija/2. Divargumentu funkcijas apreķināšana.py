# Programmas nosaukums: Divargumentu funkcijas apreķināšana
# 2. uzdevums (MPR4)
# Uzdevuma formulējums: Izveidot programmu, kura aprēķina divargumentu funkcijas vērtību.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0
print("\"Divargumentu funkcijas apreķināšana\"\nVersija 1.0\n")

print("f(x,y) = (x - y, ja x > y) un (x + y, ja citādi)\n")

x=float(input("Ievadi x skaitli ===>"))
y=float(input("Ievadi y skaitli ===>"))

if (x>y):
    print("Divargumentu funkcijas vērtiba ir x - y, ja x > y. \nRezultāts: " + str(x-y))
else:
    print("Divargumentu funkcijas vērtiba ir x + y, ja x <= y. \nRezultāts: " + str(x+y))