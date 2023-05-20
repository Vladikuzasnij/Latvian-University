# Programmas nosaukums: Datnes papildināšana un jaunas informācijas paradīšana
# 3. uzdevums (1MPR14_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas nodrošina informācijas papildināšanu teksta datnē un parāda jauno datnes saturu uz ekrāna,
# ievērojot teksta sadalījumu pa rindkopām.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


def input_lines_by_user():
    # Metode, kas paprasā lietotājam ievādīt jaunu tekstu pa rindiņam un atgriež katru rindu, kā saraksta elementu.
    # (Prasa ievadit i + 1 rindu, lai 0.rindu būtu uzrakstīta kā 1.rinda).
    # Kad tiek uzrakstīts "...", tad apstāšana.
    # Var izmantot datnes nolasīšanai un apstrādei.
    # Atgriež sarakstu, kurā katrs elements ir rindas teksts (0.elements ir 0.rindas teksts, 1.elements ir 1.rindas teksts utt.)

    lines = []
    while True:
        ievade = input(f"Ievadi {len(lines) + 1}. rindas tekstu. Ja vēlies pabeigt, ievadi \"...\": ")
        if ievade == "...":
            break
        lines.append(ievade)

    return lines


def write_to_file_list(lines, datne):
    # Ierāksta datne failā (piemēram, .txt failā) lines saraksts, kur katrs saraksta elements ir rindas teksts.
    # lines - saraksts, kur katrs saraksta elements ir rindas teksts.
    # datne - datnes fails (.txt)
    # Piemēram:
    # datne = "C:\\Users\\User\\Desktop\\teksts.txt"

    with open(datne, mode="a", encoding="utf-8") as datne:
        for line in lines:
            datne.write(line + "\n")


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


datne = "C:\\Users\\User\\Desktop\\teksts.txt"  # Ceļš līdz failām.

print("Ierakstītais teksts datnē:")  # Informācija lietotājam.
print_text_from_data_by_rows(datne)  # Parādam lietotājam, kas tagad ir ierākstīts failā.
print()  # Lai būtu atstārpe. (Glīti).

lines = input_lines_by_user()  # Izsaucam metodi, kas paprasa lietotājam ievādīt jaunu tekstu pa rindiņam.
write_to_file_list(lines, datne)  # Papildināsim "datne" failu ar "lines" sarakstu, kur katru saraksta elementu izvadīsim kā atsevišķu rindiņu.

print("\nPapildināts teksts datnē:")  # Informācija lietotājam.
print_text_from_data_by_rows(datne)  # Parādam lietotājam, kas tagad ir ierākstīts failā pēc tas papildināšanas.
