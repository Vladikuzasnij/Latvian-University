# Programmas nosaukums: Lineārās korelācijas koeficienta vērtība
# 3. uzdevums (1MPR05_Vladislavs_Babaņins)
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


def videjais_aritmetiskais(x):
    # Aprēķina masīva vidējo aritmētisko
    # x - masīvs
    n = len(x)
    t = 0
    for i in range(0, n):
        t = t + x[i]

    return t / n


def linearas_korelacijas_koeficients(x, y):
    # Aprēķina masīvu linearas korelacijas koeficientu
    # x - pirmais masīvs
    # y - otrais masīvs
    n = len(x)
    vidx = videjais_aritmetiskais(x)
    vidy = videjais_aritmetiskais(y)

    s = 0
    tx = 0
    ty = 0

    for i in range(n):
        s = s + (x[i] - vidx) * (y[i] - vidy)
        tx = tx + (x[i] - vidx) * (x[i] - vidx)
        ty = ty + (y[i] - vidy) * (y[i] - vidy)

    p = math.sqrt(tx * ty)

    if p != 0:
        return s / p
    else:
        return "Kļūda! Dalīšana ar 0"


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


m = input("Ievadiet masīva izmēru N ===> ")

while is_natural(m) == False:
    m = input("Masīva izmērs ir naturāls skaitlis!\nIevadiet masīva izmēru N ===> ")

m = int(m)
print("Ievadiet pirmā masīva skaitļus!")
t = izveidot_masivu_ar_garumu(m)
print("Ievadiet otrā masīva skaitļus!")
c = izveidot_masivu_ar_garumu(m)

print("\nPirmā skaitļu virkne:")
izvade(t)
print("Otrā skaitļu virkne:")
izvade(c)
print("Lineāras korelācijas koeficients:")
print(linearas_korelacijas_koeficients(t, c))
