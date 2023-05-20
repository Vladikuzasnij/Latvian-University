# Programmas nosaukums: N-stūra laukums ar ierakstiem
# 3.uzdevums (1MPR13_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas aprēķina N-stūra laukumu, tā virsotņu koordinātas ievadot no tastatūras.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


"""
UZDEVUMS TIKA REALIZĒTS AR IERAKSTIEM.
"""


import types
import numpy


def input_polygon_coords(n):
    # Paprasa lietotājam ievadīt virsotnes X un Y koordinātas.
    # Atgriež ierakstu a, ar lietotāja ievadītam X un Y koordinātam.
    # n - naturāls skaitlis - daudzstūra virsotņu skaits.

    for i in range(1, n + 1):
        punkts = types.SimpleNamespace()

        temp_x = input("Ievadiet " + str(i) + ". virsotnes X koordināti ==> ")
        while not is_real_check(temp_x):
            temp_x = input("Kļūda! Ievadiet reālu skaitli! Ievadiet " + str(i) + ". virsotnes X koordināti ==> ")

        temp_x = float(temp_x)

        temp_y = input("Ievadiet " + str(i) + ". virsotnes Y koordināti ==> ")
        while not is_real_check(temp_y):
            temp_y = input("Kļūda! Ievadiet reālu skaitli! Ievadiet " + str(i) + ". virsotnes X koordināti ==> ")

        temp_y = float(temp_y)

        print()

        punkts.x = temp_x
        punkts.y = temp_y

        a[i] = punkts

    return a


def area_using_shoelace_methode_list(a):
    # Aprēķina laukumu daudzstūrim, kurā punktu koordinātas ir definētas ierakstā a.
    # a - ieraksts, kurā glābajas daudzstūra koordinātas.
    # Ieraksta piemērs: [0 namespace(x=1.0, y=2.0) namespace(x=3.0, y=4.0)].
    # Atgriež daudzstūra laukumu izmantojot "Shoelace formula".

    a[0] = a[n]  # Fiktīvais punkts.

    s = 0

    for i in range(n):
        x = a[i].x + a[i + 1].x
        y = a[i].y - a[i + 1].y
        s = s + x * y

    s = abs(s) / 2

    return s


def is_real_check(n):
    # Pārbauda vai simbolu virkne ir reāls skaitlis vai nav.
    # Atgriež True, ja tas ir reāls skaitlis (float).
    # Atgriež False, ja tas nav reāls skaitlis (float).
    # n - pārbaudāma simbolu virkne.

    try:
        float(n)
    except:
        return False
    else:
        return True


def is_natural(n):
    # Pārbauda vai simbolu virkne ir naturāls skaitlis vai nav
    # Ja ir naturāls skaitlis, tad True. Ja nav tad False.
    # n - simbolu virkne, kuru pārbauda.

    if str(n).isdigit() and float(n) == int(n) and int(n) > 0:
        return True
    else:
        return False


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


n = input("Ievadiet virsotņu skaitu ==> ")
while not is_natural(n):
    n = input("Kļūda! Virsotņu skaitam ir jābūt naturālam skaitlim! Ievadiet virsotņu skaitu ==> ")
n = int(n)

a = numpy.zeros(n + 1, "O")

print()
koord_saraksts = input_polygon_coords(n)
area = area_using_shoelace_methode_list(koord_saraksts)

print("Laukums ievadītam daudzstūrim:")
print("S = " + str(area))
