# Programmas nosaukums: Skolas sekmju uzskaite ar skolēnu atzīmju ievadi un rediģēšanu
# PU1. uzdevums (1MPR14_Vladislavs_Babaņins)
# Uzdevuma formulējums: Papildināt 1.programmu, kas atļauj skolēnu atzīmju ievadi un rediģēšanu pa vienai atzīmei vienam skolēnam. (5 punkti).
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


"""
Programma tika papildināta ar rediģēšanas iespēju.
Lietotājs ievada Personas ID un tiek parādīts visu atzīmju saraksts, lietotājas ievada noteikto priekšmētu un pēc tam viņš ievāda jaunās atzīmes.
Atzīmes tika mainītas .csv failā un pēc tam tika izveidots .txt fails.

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
    # Tas atgriež vidējo atzīmi kā noapaļotu līdz veselam skaitļim.
    # (Ja nevajag apoļot, tad return average)
    # Ja atzīmju saraksts ir tukšs, tas atgriež 0.

    total = sum(grades)
    count = len(grades)
    if count == 0:
        return 0  # Gadījums, kad nav atzīmēs.
    average = total / count
    return round(average)


def generate_white_journal(student_data):
    # Ģenerē baltu žurnālu, pamatojoties uz studenta datiem.
    # Tas atgriež vārdnīcu, kurā ir priekšmeti kā atslēgas, un skolēnu vārdu un vidējo atzīmju vārdnīcu kā vērtības.
    # Atgriež baltu žurnālu.

    white_journal = {}  # Inicializējam tukšu vārdnīcu, lai saglabātu balto žurnālu.

    for student_name, data in student_data.items():  # Iterējam caur katru skolēnu student_datu vārdnīcā.
        student_class = data['Klase']  # Iegūvam skolēna klasi
        subject_grades = data['Marks']  # Iegūvam skolēna atzīmes

        for subject, grades in subject_grades.items():  # Iterējam caur katru priekšmetu un tā atbilstošās atzīmem.
            average_grade = calculate_average(grades)  # Aprēķinam katra priekšmeta vidējo atzīmi un saglabājam to baltajā žurnālā.
            if subject not in white_journal:  # Ja priekšmets vēl nav iekļauts vārdnīcā white_journal, pievienojiet to.
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


def change_student_marks(file_name, student_id, subject, new_marks):
    # Izmainā skolēna atzīmes noteiktā priekšmeta uz jaunajām.
    # Atgriež True, ja netika atrāsta neviena kļūda.
    # Atgriež False, ja tika atrāsta kļūda.
    # file_name - .csv failā ceļš
    # student_id - skolēna personas kods
    # subject - skolas priekšmēts
    # new_marks - jaunās atzīmes
    student_data = read_student_data(file_name)  # Nolasa skolēnu datus no CSV faila

    if student_id in student_data:  # Pārbauda, vai skolēna ID ir iekšā student_data
        # Iegūst skolēna informāciju un atzīmes
        student_info = student_data[student_id]
        student_grades = student_info['Marks']

        # Pārbauda, vai priekšmets pastāv skolēna atzīmēs
        if subject in student_grades:
            # Atjaunina atzīmes ar jaunajām atzīmēm
            student_grades[subject] = new_marks

            # Ieraksta atjauninātos skolēna datus atpakaļ CSV failā
            with open(file_name, 'w', newline='', encoding='utf-8-sig') as file:
                kolonnas_nosaukumi = ['Personas kods', 'Vārds', 'Uzvārds', 'Klase', 'Matemātika', 'Dabaszinības', 'Vēsture', 'Ģeogrāfija', 'Datorika']
                writer = csv.DictWriter(file, fieldnames=kolonnas_nosaukumi, delimiter=';')
                writer.writeheader()

                for student_code, student_info in student_data.items():
                    # Ieraksta skolēna informāciju un atzīmes CSV failā

                    writer.writerow({
                        'Personas kods': student_code,  # Ierakstam skolēna unikālo identifikatoru kolonnā "Personas kods".
                        'Vārds': student_info['Vārds'],  # Ailē 'Vārds' ierakstiet skolēna vārdu
                        'Uzvārds': student_info['Uzvārds'],  # Ailē 'Uzvārds' ierakstiet skolēna uzvārdu
                        'Klase': student_info['Klase'],  # Ierakstam skolēna klasi kolonnā "Klase".
                        'Matemātika': ' '.join(str(grade) for grade in student_info['Marks']['Matemātika']),  # Konvertējam un savienojam visas matemātikas atzīmes ar atstarpi atdalītā simbolu virknē un ierakstisim to rindiņa "Matemātika"
                        'Dabaszinības': ' '.join(str(grade) for grade in student_info['Marks']['Dabaszinības']),  # Konvertējam un savienojam visas dabaszīnibas atzīmes ar atstarpi atdalītā simbolu virknē un ierakstisim to rindiņa "Dabaszinības"
                        'Vēsture': ' '.join(str(grade) for grade in student_info['Marks']['Vēsture']),  # Konvertējam un savienojam visas vēstures atzīmes ar atstarpi atdalītā simbolu virknē un ierakstisim to rindiņa "Vēsture"
                        'Ģeogrāfija': ' '.join(str(grade) for grade in student_info['Marks']['Ģeogrāfija']),  # Konvertējam un savienojam visas ģeogrāfijas atzīmes ar atstarpi atdalītā simbolu virknē un ierakstisim to rindiņa "Ģeogrāfija"
                        'Datorika': ' '.join(str(grade) for grade in student_info['Marks']['Datorika'])  # Konvertējam un savienojam visas datorikas atzīmes ar atstarpi atdalītā simbolu virknē un ierakstisim to rindiņa "Datorika"
                    })

            return True  # Atgriež True, lai norādītu uz veiksmīgu skolēna atzīmju izmainīšanu

        else:
            print(f"Skolēns ar personas kodu '{student_id}' nav atrasts priekšmetā '{subject}'.")
    else:
        print(f"Skolēns ar personas kodu '{student_id}' nav atrasts.")

    return False  # Atgriež False, lai norādītu uz neveiksmigu skolēnu atzīmju izmainīšanu


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


file_name = "C:\\Users\\User\\Desktop\\student_data.csv"
student_data = read_student_data(file_name)

student_code = ""
while student_code.lower() != "nē":  # Turpinām ciklu, līdz ievade ir "nē".
    # Lūdzam lietotājam ievadīt skolēna personas kodu vai "mē", lai izietu no cikla
    student_code = input("Lūdzu, ievadiet skolēna personas kodu, kuras atzīmes gribāt izmainīt, ja negribat, tad ierakstiet \"Nē\" ==> ")
    if student_code.lower() != "nē" and student_code in student_data:  # Ja ievade nav "Nē" (neatkarīgi no reģistra) un tāds skolēns eksistē, tad...
        print_student_grades_by_code(student_data, student_code)  # ... izsaucām funkciju, lai izdrukātu skolēna atzīmes, pamatojoties uz norādīto Personas kodu

        subject = input("Lūdzu, ievadiet priekšmetu: ")  # Lūdziet lietotājam skolas priekšmētu
        if subject in student_data[student_code]['Marks']:  # Ja priekšmets pastāv skolēna "atzīmju ierakstos"
            # Lūdzam lietotājam ievadīt jaunās atzīmes, atdalot tās ar atstarpēm
            new_marks = input("Lūdzu, ievadiet jaunās atzīmes atdalītas ar atstarpi: ")
            # Pārvēršam atzīmju ievades virkni par veselu skaitļu sarakstu
            new_marks = [int(grade) for grade in new_marks.split()]
            if change_student_marks(file_name, student_code, subject, new_marks):  # Izsaucām funkciju, lai mainītu skolēna atzīmes norādītajā priekšmetā
                pass
            else:
                print("Notika neparedzēta kļūda!")  # Testēšanai
        else:
            print(f"Skolēnam ar personas kodu '{student_code}' nav atzīmes par priekšmētu '{subject}'.")  # Ja netika atrāsts
    else:
        if student_code.lower() == "nē":
            pass
        else:
            print("Kļūda! Tāds skolēns neeksistē!")
        break


file_name = "C:\\Users\\User\\Desktop\\student_data.csv"  # Aizvietojiet ar sava CSV faila nosaukumu
student_data = read_student_data(file_name)

# Ģenerējam un izdrukājam balto žurnālu
white_journal = generate_white_journal(student_data)

# Izveidojam liecību un ierakstiet to failā
testimony = generate_testimony(student_data)
file_name = "C:\\Users\\User\\Desktop\\VardsUzvards.txt"  # Aizvietojiet ar sava TXT faila nosaukumu
write_testimony_to_file(testimony, file_name)

print("\nLiecības tika uzģenerētas un ierakstītas failā VardsUzvards.txt")
