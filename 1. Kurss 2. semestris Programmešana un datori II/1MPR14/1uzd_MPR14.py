# Programmas nosaukums: Skolas sekmju uzskaite
# 1. uzdevums (1MPR14_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sekmju žurnāla izveide. Vienas skolas visu skolēnu sekmju uzskaite glabājas vārdnīca, kurā katrs skolēns tiek identificēts pēc tā personas koda (11 ciparu virkne).
# Par katru skolēnu tiek uzkrāta šāda informācija:
# 1. Vārds
# 2. Uzvārds
# 3. Klase
# 4. Mācību priekšmeti un tajos saņemtās atzīmes (mācību priekšmetu un tajos saņemto atzīmju skaitu katrai klasei nosaka programmas autors)
# Pēc skolas izveides un atzīmju ievades jāparedz, ka tiek izveidots "baltais žurnāls", kur redzamas katra skolēna gada atzīmes katrā mācību priekšmetā, kā arī
# "liecības" izveidi, ierakstot informāciju teksta datnē ar nosaukumu VardsUzvards.txt
# Testējot programmu, jāparedz, kā skolā ir vismaz 10 skolēni, kas mācās vismaz 3 dažādās klasēs un katrā klasē ir vismaz 3 mācību priekšmeti, kuros izliek vismaz 3 atzīmes. (5 punkti).
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


"""
ĒRTĪBAS PĒC PROGRAMMA TIKA IZVEIDOTI DIVI FAILI
.CSV FAILS, KURU AIZPILD PATS LIETOTĀJS AR ROKU
.TXT FAILS, KUR TIEK VEIDOTAS LIECĪBAS UN KURU IZVEIDO PROGRAMMA
TIKA REALIZĒTS TIEŠI TĀ, JO TĀ IR ĒRTĀK LIETOTĀJAM, NEVISS IEVĀDĪT PROGRAMMA ĻOTI DAUDZ SKOLĒNU VĀRDU, UZVĀRDU, PERSONAS ID UN ATZĪMES.
TĀPĒC PROGRAMMA NAV PAREDZĒTA FUNCKIJA KAS PAPRASA LIETOTĀJAM IEVĀDĪT SĒKMES VAI SKOLĒNUS.
"""

import csv


def read_student_data(file_name):
    # Šī funkcija nolasa skolēna datus no CSV faila un sakārto tos vārdnīcā.
    # file_name - ceļš līdz failām (.csv datne).
    # Piemēram:
    # file_name = "C:\\Users\\User\\Desktop\\student_data.csv"
    # Tas atgriež skolēna datu vārdnīcu.
    # return student_data

    student_data = {}  # Definējam tukšu vārdnicu

    with open(file_name, 'r', newline='', encoding='utf-8-sig') as file:
        # Datu izvilkšana no CSV rindām un kārtošana vārdnīcā
        # Katrs skolēns tiek identificēts ar unikālu  skolēna kodu

        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            # Izvelcam attiecīgos datus no katras CSV faila rindas un sakārtojam tos vārdnīcā

            student_code = row['Personas kods']  # Izvelcam skolēna unikālo ID identifikatoru (Personas kodu) no kolonnas "Personas kods"
            student_name = row['Vārds']  # Izvelcam skolēna uzvārdu no rindas "Vārds".
            student_last_name = row['Uzvārds']  # Izvelcam skolēna uzvārdu no rindas "Uzvārds".
            student_class = row['Klase']  # Izvelcam skolēna klasi no rindas "Klase".
            math_grades = [int(grade) for grade in row['Matemātika'].split()]  # Izņemam matemātikas atzīmes no rindas "Matemātika" un pārveidojam "int" skaitļos
            science_grades = [int(grade) for grade in row['Dabaszinības'].split()]  # Izņemam dabaszīnibas atzīmes no rindas "Dabaszinības" un pārveidojam "int" skaitļos
            history_grades = [int(grade) for grade in row['Vēsture'].split()]  # Izņemam vēstures atzīmes no rindas "Vēsture" un pārveidojam "int" skaitļos
            geo_grades = [int(grade) for grade in row['Ģeogrāfija'].split()]  # Izņemam ģeogrāfijas atzīmes no rindas "Ģeogrāfija" un pārveidojam "int" skaitļos
            computer_grades = [int(grade) for grade in row['Datorika'].split()]  # Izņemam datorika atzīmes no rindas "Datorika" un pārveidojam "int" skaitļos

            # Izveido vārdnīcu ar nosaukumu subject_grades, lai saglabātu katra priekšmeta atzīmes. Vārdnīca ir strukturēta šādi:
            # Priekšmets: Atzīmē priekšmeta nosaukumu ('Matemātika', 'Dabaszinības', 'Vēsture', 'Ģeogrāfija', 'Datorika').
            # Atzīmes: atspoguļo attiecīgajam mācību priekšmetam atbilstošo atzīmju sarakstu.
            subject_grades = {
                'Matemātika': math_grades,
                'Dabaszinības': science_grades,
                'Vēsture': history_grades,
                'Ģeogrāfija': geo_grades,
                'Datorika': computer_grades
            }

            # Pievienojam skolēna informāciju un atzīmes vārdnīcai student_data
            student_data[student_code] = {'Vārds': student_name, 'Uzvārds': student_last_name, 'Klase': student_class, 'Marks': subject_grades}

    return student_data


def print_student_grades_by_code(student_data, student_code):
    # Šī funkcija izdrukā skolēna atzīmes, kas identificētas pēc skolēna koda.
    # student_data: vārdnīca, kurā ir skolēna dati.
    # studenta_kods: skolēna unikālais identifikators (Skolēna ID (Personas kods)).
    # Atgriež: None

    if student_code in student_data:  # Pārbaudam, vai skolēna datu vārdnīcā ir šāds skolēna kods (vai tāds skolēns eksistē)
        student_info = student_data[student_code]  # Iegūvam informāciju par doto skolēna kodu
        student_name = student_info['Vārds']  # Iegūvam informāciju par doto skolēna vārdu
        student_surname = student_info['Uzvārds']  # Iegūvam informāciju par doto skolēna uzvārdu
        student_grades = student_info['Marks']  # Iegūvam informāciju par doto skolēna atzīmem

        print(f"Atzīmes skolēnam: {student_name} {student_surname}")  # Uzrakstām lietotājam skolēna atzīmes.

        for subject, grades in student_grades.items():  # Ejam ciklā caur katru priekšmetu un tām atbilstošam atzīmem un izdrūkam tos
            print(f"Priekšmets: {subject}, Atzīmes: {grades}")  # Izdrukājam priekšmeta nosaukumu un tā atzīmes

    else:  # Izdrukājam paziņojumu, kas norāda, ka skolēns ar norādīto kodu netika atrasts, ja netika atrāsts šāds personas kods.
        print(f"Skolēns ar personas kodu '{student_code}' nav atrāsts.")


def calculate_average(grades):
    # Aprēķina vidējo atzīmi no atzīmju saraksta.
    # Tas atgriež vidējo atzīmi kā noapaļotu līdz veselam skaitlim.
    # (Ja nevajag apoļot, tad return average)
    # Ja atzīmju saraksts ir tukšs, tas atgriež 0.

    total = sum(grades)
    count = len(grades)
    if count == 0:
        return 0  # Gadījums, kad nav atzīmēs.
    average = total / count
    return round(average)


def generate_white_journal(student_data):
    # Ģenerē baltu žurnālu, pamatojoties uz skolēna datiem.
    # Tas atgriež vārdnīcu, kurā ir priekšmeti kā atslēgas, un skolēnu vārdu un vidējo atzīmju vārdnīcu kā vērtības.
    # Atgriež baltu žurnālu.

    white_journal = {}  # Inicializējam tukšu vārdnīcu, lai saglabātu balto žurnālu.

    for student_name, data in student_data.items():  # Iterējam caur katru skolēnu student_datu vārdnīcā.
        student_class = data['Klase']  # Iegūvam skolēna klasi
        subject_grades = data['Marks']  # Iegūvam skolēna atzīmes

        for subject, grades in subject_grades.items():  # Iterējam caur katru priekšmetu un tā atbilstošās atzīmem.
            average_grade = calculate_average(grades)  # Aprēķinam katra priekšmeta vidējo atzīmi un saglabājam to baltajā žurnālā.
            if subject not in white_journal:  # Ja priekšmets vēl nav iekļauts vārdnīcā white_journal, pievienojam to.
                white_journal[subject] = {}
            white_journal[subject][student_name] = average_grade  # Pievienojam skolēna vārdu un vidējo atzīmi attiecīgajam priekšmetam baltajā žurnālā.

    return white_journal  # Atgriež baltu žurnālu.


def generate_testimony(student_data):
    # Šī funkcija ģenerē liecību, pamatojoties uz skolēna datiem.
    # Tas atgriež simbolu virkni, kas satur liecību.
    # Ja skolēnam vidēja atzīme ir 0 (visas atzīmes ir 0), tad tas priekšmēts neparadīsies (vajag ierākstīt 0 priekšmētos kurus nav skolēnam).

    testimony = ""

    for student_name, data in student_data.items():
        student_class = data['Klase']
        subject_grades = data['Marks']

        testimony = testimony + f"Liecība ID: {student_name} (Klase: {student_class}):\n"
        for subject, grades in subject_grades.items():
            average_grade = calculate_average(grades)
            if average_grade != 0:
                testimony = testimony + f"Priekšmets: {subject}, Vidējā atzīme: {average_grade}\n"
        testimony = testimony + "\n"

    return testimony


def write_testimony_to_file(testimony, file_name):
    # Ieraksta ģenerēto liecību .txt failā (file_name)
    # Tas neatgriež nekādu vērtību (atgriež None)

    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(testimony)


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


file_name = "C:\\Users\\User\\Desktop\\student_data.csv"  # Aizvietojiet ar sava CSV faila nosaukumu
student_data = read_student_data(file_name)

# TESTĒŠANAI ------------------------
# VAR PĀRBAUDĪT KATRU SKOLENU UN VIŅAS VISAS ATZĪMES
student_code = '10000000000'  # Aizstāt ar skolēna kodu, kuram vēlaties piekļūt
print_student_grades_by_code(student_data, student_code)
# TESTĒŠANAI ------------------------

# Izveidot un izdrukāt balto žurnālu
white_journal = generate_white_journal(student_data)

# Izveidot liecību un ierakstit to failā
testimony = generate_testimony(student_data)
file_name = "C:\\Users\\User\\Desktop\\VardsUzvards.txt"  # Aizvietojiet ar sava TXT faila nosaukumu
write_testimony_to_file(testimony, file_name)

print("\nLiecības tika uzģenerētas un ierakstītas failā VardsUzvards.txt")  # Informācija lietotājam
