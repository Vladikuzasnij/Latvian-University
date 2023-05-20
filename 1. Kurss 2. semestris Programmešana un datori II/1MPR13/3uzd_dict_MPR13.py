# Programmas nosaukums: N-stūra laukums ar vārdnīcām
# 3.uzdevums (1MPR13_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas aprēķina N-stūra laukumu, tā virsotņu koordinātas ievadot no tastatūras.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0

"""
UZDEVUMS TIKA REALIZĒTS AR VĀRDNĪCAM.
"""

import types


def area_using_shoelace_methode_dict(vardnica, n):
    # Aprēķina laukumu daudzstūrim, kurā punktu koordinātas ir definētas vārdnīcā, šādā veidā {"Koordinātas nosaukums" : (x, y)}.
    # Atgriež daudzstūra laukumu izmantojot "Shoelace formula".
    # vardnica - vārdnīca, kurā ir saraksts ar koordinātam šadā veidā {"Koordinātas nosaukums" : (x, y)}.
    # n - naturāls skaitlis - daudzstūra virsotņu skaits.
    # Atgriež daudzstūra laukumu.

    s = 0

    for i in range(0, n):
        # Izmantojot Gausa formulu atrodam laukumu daudzstūrim (Shoelace formula).
        x = vardnica[t[i]].x + vardnica[t[i - 1]].x
        y = vardnica[t[i]].y - vardnica[t[i - 1]].y
        s = s + x * y

    s = abs(s) / 2

    return s


def create_dict_with_coords(n):
    # Paprasa lietotājam ievadīt virsotnes nosaukumus un tā X un Y koordinātas.
    # Izveido vārdnīcu tāda veidā {"Virsotnes nosaukums" : (x, y)}, kur katru "Virsotnes nosaukums" ievada lietotājs, (x, y) arī ievada lietotājs.
    # Atgriež vārdnīcu tāda veidā  {"Virsotnes nosaukums" : (x, y)}.
    # n - naturāls skaitlis - daudzstūra virsotņu skaits.

    i = 0

    for i in range(i, n):
        name = input("Ievadiet " + str(i + 1) + ". virsotnes nosaukumu ==> ")
        punkts = types.SimpleNamespace()

        temp_x = input("Ievadiet " + str(i + 1) + ". virsotnes X koordināti ==> ")
        while not is_real_check(temp_x):
            temp_x = input("Kļūda! Ievadiet reālu skaitli! Ievadiet " + str(i + 1) + ". virsotnes X koordināti ==> ")

        temp_x = float(temp_x)

        temp_y = input("Ievadiet " + str(i + 1) + ". virsotnes Y koordināti ==> ")
        while not is_real_check(temp_y):
            temp_y = input("Kļūda! Ievadiet reālu skaitli! Ievadiet " + str(i + 1) + ". virsotnes X koordināti ==> ")

        temp_y = float(temp_y)

        punkts.x = temp_x
        punkts.y = temp_y

        vardnica.update({name: punkts})

        t.append(name)

    t.append("Fiktīvais punkts")
    vardnica["Fiktīvais punkts"] = vardnica[t[n - 1]]

    return vardnica


def is_natural(n):
    # Pārbauda vai simbolu virkne ir naturāls skaitlis vai nav
    # Ja ir naturāls skaitlis, tad True. Ja nav tad False.
    # n - simbolu virkne, kuru pārbauda.

    if str(n).isdigit() and float(n) == int(n) and int(n) > 0:
        return True
    else:
        return False


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


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


vardnica = {}
t = []

n = input("Ievadiet virsotņu skaitu ==> ")
while not is_natural(n):
    n = input("Kļūda! Virsotņu skaitam ir jābūt naturālam skaitlim! Ievadiet virsotņu skaitu ==> ")
n = int(n)

create_dict_with_coords(n)
s = area_using_shoelace_methode_dict(vardnica, n)

vardnica.pop("Fiktīvais punkts")  # izņemt no vārdnīcas atslēgu-vērtību pāri "Fiktīvais punkts".

print()
print("Punktu sarakstu izvadīšanas veids:")
print("\"Punkta nosaukums\" : (x, y)")
print(vardnica)
print("S = " + str(s))
