# Programmas nosaukums: Noteiktas izteiksmes vērtība
# 1. uzdevums (1MPR01_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas aprēķina noteiktas izteiksmes vērtību, ja N ir naturāls skaitlis,
# ko lietotājs ievada no tastatūras. Veikt ievaddatu korektuma pārbaudi.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0

def is_natural(n):
    # Pārbauda vai simbolu virkne ir naturāls skaitlis vai nav
    # Ja ir naturāls skaitlis, tad True. Ja nav tad False.
    # n - simbolu virkne, kuru pārbauda.
    if str(n).isdigit() and float(n) == int(n) and int(n) > 0:
        return True
    else:
        return False


def izteiksmes_vertiba(n):
    # Funkcija atrgriež uzdevumā norādītas izteiksmes vērtību.
    # n - naturāls skaitlis
    s = n + 1
    for i in range(n, 0, -1):
        s = i + 1 / s
    return s

# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


# Prasam ievādīt naturālo skaitli, ievādam kā simbolu virkni
n = input("Ievadiet naturalo skaitli ==> ")

# Kāmer n nav naturāls skaitlis prasam ievadit to vēlreiz
while is_natural(n) == False:
    n = input("Nav naturals skaitlis.\nIevadiet naturalo skaitli ==> ")

# Ja tas simbolu virkne ir naturāls skaitlis, tad pārveidojam to int formāta
n = int(n)

# Izsaucam funkciju, kas aprēķina izteiksmes vērtību
print("Dotas izteiksmes vērtība ir: " + str(izteiksmes_vertiba(n)))
