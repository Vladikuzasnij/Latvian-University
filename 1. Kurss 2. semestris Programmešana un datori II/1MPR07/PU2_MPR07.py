# Programmas nosaukums: Veikals
# Papilduzdevums 2 (1MPR07_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas lietotāja ievadīto reālo skaitli ( < 10 000) noapaļo līdz diviem cipariem aiz komata un rezultātu nodrukā šādā formātā:
# Ievade: 523.6789
# Izvade: Jums ir jāmaksā EUR 523.68 (pieci simti divdesmit trīs euro un 68 euro centi)
# Nepieciešami vārdi skaitļu pieraksta izveidei uzglabājami masīvā.
# Versija 1.0


import numpy


def to_vards(n):
    # Pārveido reālo skaitli no 0 līdz 9999 tā, ka tas ir izrūnāms latviešu valodā
    # n - reāls skaitlis no 0 līdz 9999
    lst_word = numpy.array(["desmit tūkstoši ", "deviņi tūkstoši ", "astoņi tūkstoši ", "septiņi tūkstoši ", "seši tūkstoši ", "pieci tūkstoši ", "četri tūkstoši ", "trīs tūkstoši ", "divi tūkstoši ", "tūkstošs ",
                            "deviņi simti ", "astoņi simti ", "septiņi simti ", "seši simti ", "pieci simti ", "četri simti ", "trīs simti ", "divi simti ", "simts ",
                            "deviņdesmit ", "astoņdesmit ", "septiņdesmit ", "sešdesmit ", "piecdesmit ", "četrdesmit ", "trīsdesmit ", "divdesmit ",
                            "deviņpadsmit ", "astoņpadsmit ", "septiņpadsmit ", "sešpadsmit ", "piecpadsmit ", "četrpadsmit ", "trīspadsmit ", "divpadsmit ", "vienpadsmit ", "desmit ",
                            "deviņi ", "astoņi ", "septiņi ", "seši ", "pieci ", "četri ", "trīs ", "divi ", "viens "])

    lst_numbers = numpy.array([10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000,
                               900, 800, 700, 600, 500, 400, 300, 200, 100,
                               90, 80, 70, 60, 50, 40, 30, 20,
                               19, 18, 17, 16, 15, 14, 13, 12, 11, 10,
                               9, 8, 7, 6, 5, 4, 3, 2, 1])

    sv = ""
    for i in range(46):
        while lst_numbers[i] <= n:
            sv = sv + lst_word[i]
            n = n - lst_numbers[i]

    if sv == "":
        return "nulle "
    else:
        return sv


def check():
    # Bezgalīgi daudz ievades. Pārbauda vai skaitlis ir reāls pozitīvs un atrodas intervālā [0, 9999]
    x = input("Ievadiet reālo pozitīvo skaitli no 0 līdz 9999 ===> ")
    while True:
        try:
            x = float(x)
        except:
            x = input("Kļūda!\nIevadiet reālo pozitīvo skaitli no 0 līdz 9999 ===> ")
        else:
            if x < 0 or x > 9999:
                x = input("Kļūda! Skaitlis nepieder intervālam [0, 9999]\nIevadiet reālo pozitīvo skaitli no 0 līdz 9999 ===> ")
            else:
                return float(x)


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


input_number = check()

input_number = round(input_number, 2)

integer_part = int(input_number)
decimal_part = int(round((input_number - integer_part) * 100))

print("\nJums ir jāmaksā EUR " + str(input_number) + " (" + str(to_vards(integer_part) + "euro un " + str(decimal_part) + " euro centi)"))
