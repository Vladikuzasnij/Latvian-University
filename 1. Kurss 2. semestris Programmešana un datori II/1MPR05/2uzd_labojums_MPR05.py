# Programmas nosaukums: Vidēja svērta vērtība
# 2. uzdevums (1MPR05_Vladislavs_Babaņins)
# Uzdevuma formulējums:  Sastādīt programmu, kas pieprasa lietotājam ievadīt divus vienāda izmēra datu masīvus ar novērojumiem un aprēķina lineārās korelācijas koeficienta vērtību starp šo abu datu masīvi atbilstošiem elementiem, ja zināms, ka to var aprēķināt pēc šādas formulas:
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


import numpy
import math


def is_natural(n):
    # Pārbauda vai simbolu virkne ir naturāls skaitlis vai nav
    # Ja ir naturāls skaitlis, tad True. Ja nav tad False.
    # n - simbolu virkne, kuru pārbauda.
    if str(n).isdigit() and float(n) == int(n) and int(n) > 0:
        return True
    else:
        return False


def izveidot_masivu_ar_garumu(n):
    # Izveido masīvu ar noradīto garumu n
    # n - naturāls skaitlis
    a = numpy.arange(n)
    for i in range(n):
        b = input("Ievadiet " + str(i) + ".elementu ===> ")
        b = is_whole(b, i)
        a[i] = b
    return a


def is_whole(x, i):  # Bezgalīgi daudz reizes ievāda
    while True:
        try:
            x = int(x)
        except:
            x = input("Kļūda! Ievadiet " + str(i) + ".elementu ===> ")
        else:
            return int(x)


def izvade(x):
    # Izvada masīva elementus pēc kārtas līdz pedējam
    # x - masīvs
    n = len(x)
    s = str(x[0])
    for i in range(1, n):
        s = s + ", " + str(x[i])
    print(s)


def videja_sverta_vertiba(x, y):
    # Aprēķina masīvu vidējo svērsto vērtību
    # x - pirmais masīvs
    # y - otrais masīvs
    n = len(x)
    t = 0
    z = 0

    for i in range(0, n):
        t = t + x[i] * y[i]

    for i in range(0, n):
        z = z + y[i]

    return t / z


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


m = input("Ievadiet masīva izmēru N ===> ")

while is_natural(m) == False:
    m = input("Masīva izmērs ir naturāls skaitlis!\nIevadiet masīva izmēru N ===> ")

m = int(m)
t = izveidot_masivu_ar_garumu(m)
print("Ievadiet elementu svarus!")
c = izveidot_masivu_ar_garumu(m)

print("\nPirmas virknes elementi:")
izvade(t)
print("Otrās virknes elementi (svars):")
izvade(c)
print("Vidēja svērta vērtība ir:")
print(videja_sverta_vertiba(t, c))
