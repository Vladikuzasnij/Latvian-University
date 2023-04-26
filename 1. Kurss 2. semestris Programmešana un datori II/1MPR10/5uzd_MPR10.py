# Programmas nosaukums: Keno loterijas izloze
# 5. uzdevums (1MPR10_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas realizē Keno loterijas izlozi un paziņo laimējošos skaitļus augošā secība.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


import random


def keno(n, m):
    # Atgriež kopu ar n-tiem nejaušiem skaitļiem kuri neatkartojas no 1 līdz m. [1, m].
    # a - set (kopa) - tukša kopa.
    # Izvēlas n skaitļus no 1 līdz m, izmantojot sets. Tie neatkartosies
    a = set()
    while len(a) < n:
        b = random.randint(1, m)
        if b not in a:
            a.add(b)

    return a


def sort_ievietosana_augosa(a):
    # Sakārto masīvu augoša secība un atgriež salīdzināšanas skaitu, lai sakārtotu masīvu
    # Kārtošanas tiek izmantota ievietošanas metode (insertion sort)
    # a - viendimensijas masīvs
    n = len(a)
    for i in range(1, n):
        if a[i - 1] > a[i]:
            x = a[i]
            j = i
            while a[j - 1] > x:
                a[j] = a[j - 1]
                j = j - 1
                if j == 0:
                    break
            a[j] = x
    return a


def print_set(a):
    # Izvada (print) uz ekrāna kopu. Bet tas to neatgriež.
    # Jāizsauc vienkarši print_set(a)
    # a - kopa (set)

    elements = sort_ievietosana_augosa(list(a))
    # Iterējam cauri elementu indeksiem un izdrukājiem tos, atdalot tos ar komatiem
    for i in range(len(elements)):
        if i == len(elements) - 1:
            # Ja elements ir pēdējais, izdrukām to bez komata
            print(elements[i])
        else:
            # Ja elements nav pēdējais, izdrukājam to ar komatu. end="", lai nebūtu pārejas uz jauno rindu kā \n
            print(str(elements[i]) + ", ", end="")


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


# Izvadam uz ekrāna laimējošos skaitļus
print("Keno loterijas izlozes laimesta skaitļi augošā secībā:")
keno = keno(20, 62)
print_set(keno)
