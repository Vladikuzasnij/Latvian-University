# Programmas nosaukums: Datnes ievade un nolasīšana
# 2. uzdevums (1MPR14_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas nodrošina informācijas ievadi teksta datnē un nolasa informāciju no teksta datnes
# un parāda to uz ekrāna, ievērojot teksta sadalījumu pa rindkopām.
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
        ievade = input(f"Ievadiet {len(lines) + 1}. rindas tekstu. Ja vēlies pabeigt, ievadi \"...\": ")
        if ievade == "...":
            break
        lines.append(ievade)

    return lines


def write_to_new_file_list(datne, lines):
    # DZĒŠ VISU SATURU NO FAILĀ un ierāksta failā "datne" (piemēram, .txt failā) lines saraksts, kur katrs saraksta elements ir rindas teksts.
    # lines - saraksts, kur katrs saraksta elements ir rindas teksts.
    # datne - datnes fails (.txt)
    # Piemēram:
    # datne = "C:\\Users\\User\\Desktop\\teksts.txt"

    with open(datne, mode="w", encoding="utf-8") as datne:
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


lines = input_lines_by_user()  # Izsaucam metodi, kas paprasa lietotājam ievādīt jaunu tekstu pa rindiņam.
datne = "C:\\Users\\User\\Desktop\\teksts.txt"  # datne - ceļš līdz failām.
write_to_new_file_list(datne, lines)  # NODZĒS VISU TEKSTU DATNĒ. Uzrakstīsim "datne" faila "lines" saraksta elementus, kur katru saraksta elementu izvadīsim kā atsevišķu rindiņu.

print("\nIerakstītais teksts datnē:")  # Ši rinda netiek ierakstīta failā, tas ir tikai informācija lietotājam.
print_text_from_data_by_rows(datne)  # Izvadām lietotājam visu tekstu no .txt failā pa rindkopam.
