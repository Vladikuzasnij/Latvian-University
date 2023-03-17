# Programmas nosaukums: Kopas mediāna
# 2. uzdevums (1MPR06_Vladislavs_Babaņins)
# Uzdevuma formulējums: Lietotājs ievada iepriekš zināma garuma nesakārtotu masīvu. Noskaidrot un izvadīt uz ekrāna šo skaitļu kopas mediānu. (1 punkts)
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


def is_whole(x, i):
    # Pārbauda vai simbolu virkne ir vesels skaitlis un ja nē, tad paprasa ievadīt to vēlreiz (bezgalīgi daudz ievādes)
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


def sort_atrais_augosa(a, sv, bv):
    # Sakārto masīvu augoša secība un atgriež salīdzināšanas skaitu, lai sakartotu masīvu
    # Kārtošanas tiek izmantota Hoara (ātrais) metode (quicksort)
    # a - viendimensijas masīvs
    # sv - sākuma vērtība
    # bv - beigu vērtība
    if sv < bv:
        i = sv
        j = bv
        solis = -1
        lv = True
        while i != j:
            if lv == (a[i] > a[j]):
                x = a[i]
                a[i] = a[j]
                a[j] = x
                x = i
                i = j
                j = x
                lv = not lv
                solis = -solis
            j = j + solis
        sort_atrais_augosa(a, sv, i - 1)
        sort_atrais_augosa(a, i + 1, bv)


def is_even_masivs(x):
    # Pārbauda vai masīva garums ir pāra skaitlis
    # Ja masīva garums ir pāra skaitlis, tad atgriež True
    # Ja masīva garums nav pāra skaitlis, tad atgriež False
    # x - viendimensijas masīvs
    masiva_garums = len(x)
    if masiva_garums % 2 == 0:
        return True
    else:
        return False


def mediana(x):
    # Atgriež masīva x mediānu
    # x - viendimensijas masīvs
    if is_even_masivs(x):
        return (x[len(x) // 2 - 1] + x[len(x) // 2]) / 2
    else:
        return x[len(x) // 2]


def izvade(x):
    # Izvada masīva elementus pēc kārtas līdz pedējam
    # x - viendimensijas masīvs
    n = len(x)
    s = str(x[0])
    for i in range(1, n):
        s = s + ", " + str(x[i])
    print(s)


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


m = input("Ievadiet masīva izmēru N ===> ")

while is_natural(m) == False:
    m = input("Masīva izmērs ir naturāls skaitlis!\nIevadiet masīva izmēru N ===> ")

m = int(m)

print("Ievadiet masīva skaitļus!")
t = izveidot_masivu_ar_garumu(m)

print("\nIevadīta skaitļu kopa:")
izvade(t)

sort_atrais_augosa(t, 0, len(t) - 1)
print("\nSakārtota skaitļu kopa:")
izvade(t)

print("\nKopas mediāna ir:\n" + str(mediana(t)))
