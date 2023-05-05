# Programmas nosaukums: Eksāmena norises simulācija
# 1. uzdevums (1MPR11_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas simulē eksāmena norisi, pieņemot, ka grupā ir 54 studenti, kas apzīmēti ar skaitļiem 1, 2, 3, ... 53, 54,
# kuriem tiek piedāvātas 26 eksāmena biļetes, kas apzīmētas ar lielajiem latīņu alfabēta burtiem.
# Eksāmenu sāk 10 uz labu laimi izvelēti, studenti, kuri katrs saņem tiešu vienu no 26 piedāvātajām biļetēm.
# Kad 1. students atbildējis, viņa biļete tiek atlikta atpakaļ eksāmena biļešu "kaudzē" un nāk nākamais students un izvēlās uz labu laimi vienu eksāmena biļeti no eksāmena biļešu "kaudzes".
# Tā process tiek atkārtots, kamēr visi studenti ir noeksaminēti. Paziņot uz ekrāna, kādā secība studenti tika eksaminēti un kādu eksāmena biļeti katrs students saņēma.
# NB! Uzdevuma atrisināšanai jāizmanto kopas.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


import random


def choose_pair(students_prepare):
    # Atgriež pirmu masīva students_prepare lementu un nodzes to no saraksta students_prepare.
    # students_prepare - saraksts (list) ar studentiem telpā (kuri gatavojas eksāmenam un sež ar biļētem).
    # students_prepare ir saraksts ar kortēžiem iekšā. [(studenta numurs, biļete), (studenta numurs, biļete), ... (studenta numurs, biļete)],

    first_pair = students_prepare[0]  # Paņem pirmo kortēžu ar studentu un biļeti.
    students_prepare.remove(first_pair)  # Nodzēs studentu no saraksta kuri gatavojas (jo viņš jau atbild),
    return first_pair


def choose_random_pair(students_prepare, students, exam_tickets):
    # Atgriež nejaušu (student, exam_ticket) kortēžu, no saraksta students (studenti, kas vel nav nokārtojusi eksāmenu un vēl nav eksāmena telpā).
    # Nejauši izvēlas studentu no tiem, kas vēl nav nokārtojusi eksāmenu un nesež telpā. Atgriež kortežu ar studentu un eksāmena biļeti. (student, exam_ticket),
    # students_prepare - saraksts (list) ar studentiem telpā (kuri gatavojas eksāmenam un sež ar biļētem).
    # students - kopa ar visiem studenti kuri nav eksāmena telpā un pagaidam nav nokārtojusi eksāmenu.
    # exam_tickets - kopa ar visam biļetem no A līdz Z.

    if len(students) == 0:
        return None
    student = students.pop()
    exam_ticket = exam_tickets.pop()
    return (student, exam_ticket)


def print_pairs(pairs):
    # Glīti izvāda sarakstu pairs, kas reprēzentē studentus ar biļētem kuri sēž telpā un gatavojas eksāmenam.
    # Piemērs:
    # Ievade tāds saraksts: [(36, S), (50, T), (37, D), (42, R), (19, W), (22, U), (41, M), (44, Q), (52, P), (38, H)].
    # Funkcija atgriež tādu simbolu virkni: 36-S, 50-T, 37-D, 42-R, 19-W, 22-U, 41-M, 44-Q, 52-P, 38-H
    # pairs - saraksts ar kortežiem ar divam vērtībam [(students, biļete), (students, biļete), ... , (students, biļete)].

    for i in range(len(pairs)):
        if i == len(pairs) - 1:
            print(str(pairs[i][0]) + "-" + str(pairs[i][1]))
        else:
            print(str(pairs[i][0]) + "-" + str(pairs[i][1]) + ", ", end="")


def convert_int_to_str_in_set_in_range(n, m, kopa):
    # Metode (neko neatgriež), kura izmaina visas int vērtības kopā uz str.
    # Piemēram:
    # {5, 33, 14, 13, 11} -> {'5', '33', '14', '13', '11'}.
    # convert_int_to_str_in_set_in_range(1, 55, students).
    # kopa - set, kopa, kurai gribāt visas int vērtības izmainīt uz str. Piemēram: 1 -> "1"
    # n - int, no cik (parasti no 1).
    # m - int, līdz cik līdz m-1 (šeit līdz 55, bet funkcijai izmainīs int uz str līdz 54).

    for i in range(n, m):
        kopa.add(str(i))


def exam_tickets_words_in_range(n, m, exam_tickets):
    # Metode (neko neatgriež), kura piepildina tukšo kopu exam_tickets ar simboliem no ASCII koda no n līdz m str veidā.
    # exam_tickets - tukša kopa, kurai jābut kopai ar eksāmena biļētiem no A līdz Z.
    # n - int, no cik (ASCII kods simbols).
    # m - int, līdz cik (ASCII kods).
    # (65, 91) - lielajiem latiņu burtiem.
    # Piemērs: exam_tickets_words_in_range(65, 91, exam_tickets).

    for i in range(n, m):
        exam_tickets.add(chr(i))


def start_students_number(n, students, exam_tickets):
    # Atgriež students_prepare sarakstu, kura sastav no kortēžiem [(student, exam_ticket), (student, exam_ticket), ... , (student, exam_ticket)].
    # un šeit ir n šādu kortežu (student, exam_ticket).
    # n - int, cik "start" studentus paņemt? (10 šajā gadījumā). Tas ir cik studentus "izlozēsim" kartot eksāmenu pirmājiem.
    # students - set, kopa ar visiem studentiem, kuri nav ienākuši eksāmenas telpā un vēl nav nokārtojusi eksāmenu. No viņiem paņemsim pirmus 10 studentu.
    # exam_tickets - set, kopa ar visiem eksāmena biļētem, kuri nav pie studentiem.

    for i in range(n):
        student = students.pop()
        exam_ticket = exam_tickets.pop()
        students_prepare.append((student, exam_ticket))
    return students_prepare


def exam_simulation(students_prepare):
    # Simulē eksāmena norisināšanas.
    # students_prepare - saraksts veidā [(student, exam_ticket), (student, exam_ticket), ... , (student, exam_ticket)].
    # Kad 1. students atbildējis, viņa biļete tiek atlikta atpakaļ eksāmena biļešu "kaudzē" un nāk nākamais students un izvēlās uz labu laimi vienu eksāmena biļeti no eksāmena biļešu "kaudzes".
    # Tā process tiek atkārtots, kamēr visi studenti ir noeksaminēti.
    # Paziņo uz ekrāna, kādā secība studenti tika eksaminēti un kādu eksāmena biļeti katrs students saņēma.

    exam = True  # Karogs ir True, kamēr students_prepare != 0 (kāmer eksamenācijas telpā ir palikuši cilvēki, tad eksāmens turpinās).
    while exam:  # Kamēr eksāmens ir True
        if len(students_prepare) == 0:  # Ja nav nevienu cilvēku eksamenācijas telpā, tad eksāmens beidzās.
            print("Eksāmens beidzās!")
            exam = False  # eksāmens beidzās.
        else:
            pair = choose_pair(students_prepare)  # Izvēlas pirmo pāriti (kreiso parīti) (students, biļete) no studentiem, kuri gatavojas eksāmenam un sež telpā ar biļetem.
            print("Atbild " + str(pair[0]) + ". students ar biļeti " + str(pair[1]) + ".")  # Izvadam informāciju, kurš students atbild (kreisāis) un ar kādu biļeti viņš ir.
            exam_tickets.add(pair[1])  # Pievienojam biļeti no korteža eksāmena biļetes kaudzītei (studenta biļeti, kurš ir atbildējis uz jautājumu).
            print("Biļete", pair[1], "tiek atlikta biļešu \"kaudzē\".\n")  # Izvadam informāciju, kura biļete tika atlikta kaudzē.

            if len(students) == 0:  # Ja visi studenti jau ir ienākuši eksāmenā telpā, tad jau mēs vairs nevienu neaicināsim atkāl uz eksāmenu. (jo tie ir pēdējie studenti, kuri karto eksāmenu).
                print_pairs(students_prepare)  # Glīti izvadīt informāciju lietotājam par to, kuri cilvēki sēž un gatavojas eksāmenam iekšā telpā.
                pair = choose_pair(students_prepare)  # Izvēlas pirmo pāriti (kreiso parīti) (students, biļete) no studentiem, kuri gatavojas eksāmenam un sež telpā ar biļetem.
                print("Atbild " + str(pair[0]) + ". students ar biļeti " + str(pair[1]) + ".")  # Izvadam lietotājam informāciju, kurš students atbild un ar kādu biļeti.
                exam_tickets.add(pair[1])  # Pievienojam biļeti no korteža eksāmena biļetes kaudzītei (studenta biļeti, kurš ir atbildējis uz jautājumu).
                print("Biļete", pair[1], "tiek atlikta biļešu \"kaudzē\".\n")  # Izvadam informāciju, kura biļete tika atlikta kaudzē.
                print_pairs(students_prepare)  # Glīti izvadīt informāciju lietotājam par to, kuri cilvēki sēž un gatavojas eksāmenam iekšā telpā.

            else:
                atnac = choose_random_pair(students_prepare, students, exam_tickets)  # Ja nav visi studenti ir ienākuši eksāmenā telpā, tad vajag aicināt nākamos (atnac) studentus uz eksāmenu (jo tie ir palikuši un vēl nenokārtoja eksāmenu). Nejauši izvelāmies studentu un viņam biļēti, no tiem, kuri vēl nav nokārtojuši.
                print("Atnāc " + str(atnac[0]) + ". students un izvilka biļeti " + str(atnac[1]) + ".")  # Izvadam lietotājam informāciju, kurš students atnāca un kādu biļeti paņēma.
                students_prepare.append(atnac)  # Pievienojam sarakstam ar kortēžiem students_prepare [(student, exam_ticket), (student, exam_ticket), ... , (student, exam_ticket)] jauno kortēžu, ar studentu kurš atnāca un izvēlējas biļeti.
                print_pairs(students_prepare)  # Glīti izvadīt informāciju lietotājam par to, kuri cilvēki sēž un gatavojas eksāmenam iekšā telpā.


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


students = set()  # Tukša kopa ar visiem studentiem, tā tiek piepildīta ar str numuriem vēlāk šeit "convert_int_to_str_in_set_in_range(1, 55, students)".
exam_tickets = set()  # Tukša kopa ar visiem eksāmena biļētem (kaudzē ar biļetem). Tā tiek piepildīta ar str burtiem no A līdz Z šeit "exam_tickets_words_in_range(65, 91, exam_tickets)".
students_prepare = []  # Tukšais saraksts, kur glābāsies visi kortēži [(studentu, biļeti), (studentu, biļeti), ... (studentu, biļeti)]. Tas tiek piepildīts ar start_students_number.

convert_int_to_str_in_set_in_range(1, 55, students)  # Lai visi skaitļi kopā, būtu uztvērti ka simbolu virknes (str). Citādi pop funkcijas nestrādās pareizi.
exam_tickets_words_in_range(65, 91, exam_tickets)  # Izveido biļetes numurus no A līdz Z. Tā tiek piepildīta ar str burtiem no A līdz Z.

# print("Studentu kopa:", students) # TESTĒŠANAI.
# print("Eksāmena biļešu kopa:", exam_tickets) # TESTĒŠANAI.

start_students_number(10, students, exam_tickets)  # Izveido sakotnēju studentu sarakstu ar [(studentu, biļeti), (studentu, biļeti), ... (studentu, biļeti)].
print("Eksāmena simulācija.\nFormāts: ([Studenta numurs]-[Izvilkta biļete])\n")  # Paskaidrojums lietotājam.
print("Pirmie desmit studenti ar izvilktam biļētem:")  # Informācija lietotājam.

print_pairs(students_prepare)  # Glīti izvada pirmus 10 studentus.
exam_simulation(students_prepare)  # Sākt eksāmenu.
