# Programmas nosaukums: Trīs masīvu apvienošana
# 4. uzdevums (1MPR07_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas doto naturālo skaitli no 1 līdz 3899 arābu pierakstā pārveido par skaitļi romiešu pierakstā.
# Cipari romiešu pierakstā jāuzglabā masīvā.
# Versija 1.0


import numpy


def to_roman(n):
    # Pārveido veselo skaitli no 1 līdz 3899 no arābu pieraksta uz romiešu pierakstu
    # n - naturāls skaitlis no 1 līdz 3899
    romas = numpy.array(["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", 'I'])
    vertibas = numpy.array([1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1])
    sv = ""
    for i in range(13):
        while vertibas[i] <= n:
            sv = sv + romas[i]
            n = n - vertibas[i]
    return sv


def is_natural_and_interval(n):
    # Pārbauda vai simbolu virkne ir naturāls skaitlis vai nav
    # Ja ir naturāls skaitlis, tad True. Ja nav tad False.
    # n - simbolu virkne, kuru pārbauda.
    if (str(n).isdigit() and float(n) == int(n) and int(n) > 0):
        if (int(n) < 1 or int(n) > 3899):
            return False
        else:
            return True
    else:
        return False


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


n = input("Ievadiet naturālo skaitli no 1 līdz 3899 ==> ")

while is_natural_and_interval(n) == False:

    n = input("Kļūda! \nIevadiet naturālo skaitli no 1 līdz 3899 ==> ")

n = int(n)

print("\nArābu -> Romiešu")
print(str(n) + ": " + str(to_roman(n)))

