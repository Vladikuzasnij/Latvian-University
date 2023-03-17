# Programmas nosaukums: Pērlīšu vēršanas uzdevums.
# 5. uzdevums (1MPR03_Vladislavs_Babaņins)
# Uzdevuma formulējums: Zināms, ka vienai zilai pērlītei var pievienot tieši 2 sarkanas, 1 zilu un 3 oranžas pērlītes;
# vienai sarkanai pērlītei var pievienot tieši 3 sarkanas, 2 zilas un 1 oranžu pērlīti;
# vienai oranžai pērlītei var pievienot tieši 2 sarkanas, 3 zilas un 1 oranžu pērlīti;
# pērlītes tiek izkārtotas pa rindiņām, un katrā nākamajā rindiņā esošās pērlītes ir visu iepriekšējā rindiņā esošo pērlīšu “pēcteči”.
# Sastādīt programmu, kas noskaidro cik un kādas krāsas pērlītes ir N-tajā rindiņā. Skaitli N ievada lietotājs.
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


def zila(N, krasa):
    # Skaita cik ir zīlas krāsas pērlītes N rindā
    # N - N rindā
    # krasa - "z" - zīla, "s" - sarkana, "o" - oranža
    if N == 1:
        if krasa == "z":
            return 1
        else:
            return 0
    else:
        return 2 * sarkana((N - 1), krasa) + zila((N - 1), krasa) + 3 * oranzs((N - 1), krasa)


def sarkana(N, krasa):
    # Skaita cik ir sarkanas krāsas pērlītes N rindā
    # N - N rindā
    # krasa - "z" - zīla, "s" - sarkana, "o" - oranža
    if N == 1:
        if krasa == "s":
            return 1
        else:
            return 0
    else:
        return 3 * sarkana((N - 1), krasa) + 2 * zila((N - 1), krasa) + 2 * oranzs((N - 1), krasa)


def oranzs(N, krasa):
    # Skaita cik ir oranžas krāsas pērlītes N rindā
    # N - N rindā
    # krasa - "z" - zīla, "s" - sarkana, "o" - oranža
    if N == 1:
        if krasa == "o":
            return 1
        else:
            return 0

    else:
        return sarkana((N - 1), krasa) + 3 * zila((N - 1), krasa) + oranzs((N - 1), krasa)


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


krasa = input("Ievadiet pirmā pērliša krāsu!\n'z' (zilā), 's' (sarkanā), 'o' (oranžā) ==> ")

while krasa != "s" and krasa != "z" and krasa != "o":
    krasa = input("Tika ievadīti nekorekti dati.\nIevadiet pirmā pērliša krāsu!\n 'z' (zilā), 's' (sarkanā), 'o' (oranžā) ==> ")

N = input("Ievadiet rindas numuru ==> ")

while is_natural(N) == False:
    N = input("Tika ievadīti nekorekti dati.\nIevadiet rindas numuru ==> ")

N = int(N)

# Izvada pērlīšu skaitu katra krāsā N rindā
print("Sarkanas pērlītes:", sarkana(N, krasa))
print("Zilās pērlītes:", zila(N, krasa))
print("Oranžas pērlītes:", oranzs(N, krasa))
