# Programmas nosaukums: Vienas datnes informāciju pārkopēšanu otrā jaunā teksta datnē
# 4. uzdevums (1MPR14_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas nodrošina informācijas pārrakstīšanu (pārkopēšanu) no vienas teksta datnes otrā jaunā teksta datnē.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


def tekstu_parkopesena_no_datne1_to_datne2(datne1, datne2):
    # Pārkope tekstu no datne1 -> datne2.
    # Atgriež None
    # datne1 - no kurā failā gribām paņemt informāciju.
    # datne2 - kurā failā gribām informāciju no datne1 pārkopēt.
    # Piemēram:
    # datne1 = "C:\\Users\\User\\Desktop\\teksts.txt"
    # datne2 = "C:\\Users\\User\\Desktop\\teksts2.txt"

    with open(datne1, mode="r", encoding="utf-8") as datne1:
        with open(datne2, mode="w", encoding="utf-8") as datne2:
            for rinda in datne1:
                datne2.write(rinda)


def print_text_from_data_by_rows(datne):
    # Uzrakstā termināla lietotājam visu tekstu no .txt failā pa rindam.
    # datne - datnes fails (piemēram, .txt fails)
    # Piemēram:
    # datne = "C:\\Users\\User\\Desktop\\teksts.txt"

    with open(datne, mode="r", encoding="utf-8") as datne:
        for rinda in datne:
            print(rinda, end='')


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


# Ceļi līdz failiem
datne1 = "C:\\Users\\User\\Desktop\\teksts.txt"
datne2 = "C:\\Users\\User\\Desktop\\teksts2.txt"

print("Ierakstītais teksts 1.datnē:")  # Informācija lietotājam.
print_text_from_data_by_rows(datne1)  # Parādam lietotājam kāda informācija ir ierākstīta failā datne1 (no kurā kopēsim informāciju).
print("\n")  # Lai būtu glīti lietotājam.


print("Ierakstītais teksts 2.datnē:")  # Informācija lietotājam.
print_text_from_data_by_rows(datne2)  # Parādam lietotājam kāda informācija ir ierākstīta failā datne2 (uz viņu mēs kopēsim informāciju).
print("\n")  # Lai būtu glīti lietotājam.

tekstu_parkopesena_no_datne1_to_datne2(datne1, datne2)  # Veicām pārkopēšanu.

print("Ierakstītais teksts 2.datnē pēc pārrakstīšanas:")  # Informācija lietotājam.
print_text_from_data_by_rows(datne2)  # Parādam lietotājam kāda informācija ir ierākstīta failā datne2 pēc pārkopēšanas (jābut informācijai no datne1).
