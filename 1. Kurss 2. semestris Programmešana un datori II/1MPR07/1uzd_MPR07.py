# Programmas nosaukums: Apvienot divus masīvus augoša secībā lineārā laikā
# 1. uzdevums (1MPR07_Vladislavs_Babaņins)
# Uzdevuma formulējums: Lietotājs ievada divus dažāda garuma augošā secībā sakārtotus masīvus.
# Lineārā laikā apvienot abus masīvus vienā augoša secībā sakārtotā masīvā un izvadīt to uz ekrāna.
# Versija 1.0

import numpy


def izveidot_masivu_ar_garumu(n):
    # Izveido masīvu ar noradīto garumu n
    # n - naturāls skaitlis
    a = numpy.arange(n)
    for i in range(n):
        b = input("Ievadiet " + str(i) + ".elementu ===> ")
        b = is_whole(b, i)
        a[i] = b
    return a


def izvade(x):
    # Izvada masīva elementus pēc kārtas līdz pedējam
    # x - viendimensijas masīvs
    n = len(x)
    s = str(x[0])
    for i in range(1, n):
        s = s + ", " + str(x[i])
    print(s)


def is_whole(x, i):
    # Pārbauda vai simbolu virkne ir vesels skaitlis un ja nē, tad paprasa ievadīt to vēlreiz (bezgalīgi daudz ievades)
    # Ja simbolu virkne ir vesels skaitlis, tad atgriež to kā int(x)
    # x - pārbaudāma simbolu virkne
    # i - i-tajs elements
    while True:
        try:
            x = int(x)
        except:
            x = input("Kļūda! Ievadiet " + str(i) + ".elementu ===> ")
        else:
            return int(x)


def is_natural(n):
    # Pārbauda vai simbolu virkne ir naturāls skaitlis vai nav
    # Ja ir naturāls skaitlis, tad True. Ja nav tad False.
    # n - simbolu virkne, kuru pārbauda.
    if str(n).isdigit() and float(n) == int(n) and int(n) > 0:
        return True
    else:
        return False


def apvieno(a, b):
    # Apvieno divus sakartotus masīvus a un b, un sakārto tos
    # Lineāra laiks o(n)
    # a - viendimensijas masīvs
    # b - viendimensijas masīvs
    ga = len(a)
    gb = len(b)
    gc = ga + gb
    c = numpy.arange(gc)
    ia = 0
    ib = 0
    ic = 0
    while (ia < ga) and (ib < gb):
        if a[ia] < b[ib]:
            c[ic] = a[ia]
            ia = ia + 1
        else:
            c[ic] = b[ib]
            ib = ib + 1
        ic = ic + 1
    if ia < ga:
        for i in range(ia, ga):
            c[ic] = a[i]
            ic = ic + 1
    else:
        for i in range(ib, gb):
            c[ic] = b[i]
            ic = ic + 1
    return c


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


m = input("Ievadiet 1. masīva izmēru ===> ")

while is_natural(m) == False:
    m = input("Masīva izmērs ir naturāls skaitlis!\nIevadiet masīva izmēru N ===> ")

m = int(m)

print("\nIevadiet sakārota augošā secība masīva skaitļus!")
a = izveidot_masivu_ar_garumu(m)


n = input("\nIevadiet 2. masīva izmēru ===> ")

while is_natural(n) == False:
    n = input("Masīva izmērs ir naturāls skaitlis!\nIevadiet masīva izmēru N ===> ")

n = int(n)

print("\nIevadiet sakārota augošā secība masīva skaitļus!")
b = izveidot_masivu_ar_garumu(n)

print("\nPirmais augošā secība sakārtots masīvs:")
izvade(a)

print("\nOtrais augošā secība sakārtots masīvs:")
izvade(b)

c = apvieno(a, b)

print("\nApvienots augošā secība sakārtots masīvs:")
izvade(c)
