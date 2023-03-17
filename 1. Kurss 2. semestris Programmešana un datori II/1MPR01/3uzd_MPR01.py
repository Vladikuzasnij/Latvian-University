# Programmas nosaukums: Noteiktas izteiksmes vērtība
# 3. uzdevums (1MPR01_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas aprēķina izteiksmes arcsin(x) vērtību ar precizitāti 10^(-6), ka zināms, ka
# ja zināms, ka abs(x) < 1 un to lietotājs ievada no tastatūras, pieņemot, ka izteiksmes precizitāti nosaka pēdējais saskaitāmais.
# Pārbaudīt ievades datu korektumu
# Programmas autors: Vladislavs Babaņins
# Versija 1.0

import math


def arcsin(x, PR):
    # Atgriež arcisn(x) vērtību
    # x - arcins(x) - funkcijas arguments
    # PR - precizitāte (nosaka pedējais saskaitamais)
    n = 0
    s = x
    y = x
    while abs(y / (n + 1)) > PR:
        n = n + 2
        y = y * x * x * (n - 1) / n
        s += y / (n + 1)
    return s


def is_real_and_abs_mazaks_neka_viens(n):
    # Pārbauda vai simbolu virkne n ir reāls skaitls un abs(n) < 1
    # Atgriež True, ja izpildas abi nosacījumi.
    # Atgriež "Nav reals skaitlis", ja simbolu virkne n nav reāls skaitlis
    # Atgriež "Ir reals skaitlis, bet abs(n) >= 1", ja ja simbolu virkne ir reāls skaitlis, bet abs(n) >= 1
    # n - simbolu virkne
    try:
        n = float(n)
    except:
        return "Nav reals skaitlis"
    else:
        n = float(n)
        if abs(n) >= 1:
            return "Ir reals skaitlis, bet abs(n) >= 1"
        else:
            return True


def is_real(n):
    # Pārbauda vai simbolu virkne ir reāls (racionāls) skaitlis vai nav
    # Ja ir reāls skaitlis, tad True. Ja nav tad False.
    # n - simbolu virkne, kuru pārbauda.
    try:
        n = float(n)
    except:
        return False
    else:
        return True

# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


x = input("Ievadi funkcijas argumentu x ===> ")

while is_real_and_abs_mazaks_neka_viens(x) == "Nav reals skaitlis" or is_real_and_abs_mazaks_neka_viens(x) == "Ir reals skaitlis, bet abs(n) >= 1":
    if is_real_and_abs_mazaks_neka_viens(x) == "Nav reals skaitlis":
        x = input("Kļūda! Nav reāls skaitlis\nIevadiet reālo skaitli ==> ")
    else:
        x = input("Kļūda! abs(x) >= 1\nIevadiet tādu reālo skaitli x, lai abs(x) < 1 ==> ")

PR = 0.000001
x = float(x)
result = arcsin(x, PR)
round_result = round(result, 6)
print("arcsin(" + str(x) + ") = " + str(round_result) + " radiāni, ar precizitāti " + str(PR))
print("arcsin(" + str(x) + ") = " + str(round(round_result / math.pi * 180, 6)) + " grādi, ar precizitāti " + str(PR))

