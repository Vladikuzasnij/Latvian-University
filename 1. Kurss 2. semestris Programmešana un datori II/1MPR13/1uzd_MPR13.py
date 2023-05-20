# Programmas nosaukums: Sudoku spēles lapiņa korektas aizpildīšanas pārbaude
# 1. uzdevums (1MPR13_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas pārbauda vai Sudoku spēles lapiņa ir aizpildīta korekti. (2 punkti)
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


import numpy


def fill_array_randomly(n, m):
    # Nejauši aizpilda n x m matricu ar naturāliem skaitļiem no 1 līdz 9.
    # [1, 2, 3, 4, 5, 6, 7, 8, 9].
    # n - rindu skaits matricā (sudoku ir 9 rindas) (int).
    # m - kolonnu skaits matricā (sudoku ir 9 kolonnas) (int).
    # Atgriež aizpildīto masīvu ar nejaušiem naturāliem skaitļiem no 1 līdz 9.

    # Izveidojam tukšu 9x9 divdimensijas masīvu (matricu).
    a = numpy.zeros((n, m), dtype=int)

    # Ejam ciklā cauri katrai masīva rindai un kolonnai.
    for i in range(n):
        for j in range(m):
            # Ģenerējam nejaušu naturālu skaitli no 1 līdz 9.
            random_number = numpy.random.randint(1, 10)
            # Piešķiram [i][j] vietā nejaušu naturālu skaitli no 1 līdz 9.
            a[i][j] = random_number

    # Atgriež aizpildīto masīvu ar nejaušiem naturāliem skaitļiem no 1 līdz 9.
    return a


def check_array_rows_and_columns(a):
    # Pārbauda vai matricā katra rindā un kolonnā visi skaitļi ir dažādi, izmantojot kopas.
    # Atgriež True, ja visi skaitļi visas rindas un kolonnas ir dažādi.
    # Atgriež False, ja ir kādi divi skaitļi kāda rinda vai kolonna kuri sakrīt.
    # a - divdimensijas masīvs (matrica).

    for i in range(9):
        # Pārbauda, vai katrā rindā nav skaitļu dublikātu (nav vienādu skaitļu).
        # Izmantojam kopas. Ja kopā nav ar gārumu 9, tad ir cipari kas atkartojas.
        if len(set(a[i])) != 9:
            print(str(i + 1) + ". rindā ir cipari, kas atkārtojas.")  # Izvadam, kur tika atrāsta kļūda.
            return False

    for j in range(9):
        # Pārbauda, vai katrā kolonnā nav skaitļu dublikātu (nav vienādu skaitļu).
        # Izmantojam kopas. Ja kopā nav ar gārumu 9, tad ir cipari kas atkartojas.
        col_numbers = [a[i][j] for i in range(9)]
        if len(set(col_numbers)) != 9:
            print(str(j + 1) + ". kolonnā ir cipari, kas atkārtojas.")
            return False

    return True


def check_submatrix(matrix, i, j):
    # Atgriež True ja 3x3 apakšmatricā (apakšmatricas ir paradītas zemāk) visi skaitļi ir dažādi.
    # Atgriež False ja 3x3 apakšmatricā kādi divi skaitļi ir vienādi.
    # Sudoku 3x3 apakšmatricas.
    # matrix - pilnā 9x9 matrica (divdimensijas masīvs).
    # i - no kuras rīndas sāksim (int).
    # j - no kuras kolonnas sāksim (int).

    submatrix = []
    for row in range(i, i + 3):
        for col in range(j, j + 3):
            submatrix.append(matrix[row][col])
    return len(set(submatrix)) == 9


def check_3x3_submatrixes(a):
    # Pārbaudam katru 3x3 apakšmatricu un paziņojam lietotājam kāda apakšmatrica skaitļi ir dažādi un kurā ir vienādi.
    # Izsauc check_submatrix(a, i, j) un paziņo lietotājam "Visi skaitļi apakšmatricā [{i//3 + 1}][{j//3 + 1}] ir atšķirīgi.",
    # vai "Ne visi skaitļi apakšmatricā [{i//3 + 1}][{j//3 + 1}] ir atšķirīgi."
    # Atgriež True, ja nav nevienas apakšmatricas, kurai iekšā ir divi vienādi skaitļi.
    # Atgriež False, ja ir kaut viena apakšmatrica, kurai iekšā ir divi vienādi skaitļi.
    # a - divdimensiju masīvs.

    # Sudoku deviņas apakšmatricas:
    # [0][0] [0][1] [0][2]   [0][3] [0][4] [0][5]   [0][6] [0][7] [0][8]
    # [1][0] [1][1] [1][2]   [1][3] [1][4] [1][5]   [1][6] [1][7] [1][8]
    # [2][0] [2][1] [2][2]   [2][3] [2][4] [2][5]   [2][6] [2][7] [2][8]

    # [3][0] [3][1] [3][2]   [3][3] [3][4] [3][5]   [3][6] [3][7] [3][8]
    # [4][0] [4][1] [4][2]   [4][3] [4][4] [4][5]   [4][6] [4][7] [4][8]
    # [5][0] [5][1] [5][2]   [5][3] [5][4] [5][5]   [5][6] [5][7] [5][8]

    # [6][0] [6][1] [6][2]   [6][3] [6][4] [6][5]   [6][6] [6][7] [6][8]
    # [7][0] [7][1] [7][2]   [7][3] [7][4] [7][5]   [7][6] [7][7] [7][8]
    # [8][0] [8][1] [8][2]   [8][3] [8][4] [8][5]   [8][6] [8][7] [8][8]

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if check_submatrix(a, i, j):
                print(f"Visi skaitļi apakšmatricā [{i//3 + 1}][{j//3 + 1}] ir atšķirīgi.")
            else:
                print(f"Kļūda! Apakšmatricā [{i//3 + 1}][{j//3 + 1}] ir divi vienādi skaitļi!")
                return False
    return True


def input_sudoku_matrix():
    # Paprasa lietotājam ievādīt veselu skaitļi no 1 līdz 9 katrai "šūnas" vērtībai 9x9 matricai.
    # Atgriež aizpildītu ar lietotāja ievādītam vērtībam matricu ar veseliem skaitļiem no 1 līdz 9.
    # Ejam ciklā caur katru masīva rindu un kolonnu.

    for i in range(9):
        for j in range(9):
            # Turpinam palūgt ievadi, līdz tiek norādīts derīgs skaitlis (cipars no 1 līdz 9).
            while True:
                # Palūdzam lietotājam ievadīt pašreizējās pozīcijas skaitļi (cipars no 1 līdz 9).
                number = input("Ievadiet veselu skaitli no 1 līdz 9 pozīcijai [" + str(i) + "][" + str(j) + "]: ")
                # Pārbaudam, vai ievadītais skaitlis ir no 1 līdz 9 un vai vispār tas ir cipars.
                if number.isdigit() and 1 <= int(number) <= 9:
                    # Konvertējam ievadi par veselu skaitli un piešķiram to masīvam.
                    a[i][j] = int(number)
                    break
                else:
                    print("Nepareiza ievade! Lūdzu, ievadiet veselu skaitli no 1 līdz 9.")

    # Agriež aizpildītu ar lietotāja ievādītam vērtībam matricu ar veseliem skaitļiem no 1 līdz 9.
    return a


def matrix_to_string_float_3x3(matrix):
    # Atgriež matricas virknes attēlojumu, kur katra rinda ir atdalīta ar \n un izlīdzināta atbilstoši maksimālās vērtības garumam.
    # Ja vērtība ir vesels skaitlis, tā tiek parādīta bez komata. Pretējā gadījumā tas tiek parādīts ar decimālzīmi.
    # Funkcija arī atrod maksimālo vērtību garumu matricā un aizpilda nepieciešamās atstarpes " ", lai tās glīti izlīdzinātu (glītas atkāpes).
    # Ja matricā ir 0, tas tiek aizstāts ar simbolu ∙.
    # matrix - matrica (divdimensiju numpy masīvs ar izmēriem n x m).

    # Piemērs, kāda veida tiek atgriezta simbolu virkne:
    # 1 6 3  9 3 4  3 6 6
    # 4 9 9  2 7 3  9 9 5
    # 3 5 9  5 2 7  9 7 4
    #
    # 4 6 6  3 3 8  2 5 3
    # 1 5 6  8 9 2  4 8 3
    # 9 3 9  6 8 7  2 8 2
    #
    # 7 4 9  3 9 3  7 1 1
    # 1 3 5  2 6 3  1 3 1
    # 6 5 3  8 9 7  7 1 8

    rindas = len(matrix)
    kolonnas = len(matrix[0])
    max_len = 0

    for i in range(rindas):  # atrod max_len, lai noteiktu nepieciešamo atkāpi.
        for j in range(kolonnas):
            number = matrix[i][j]
            if number == int(number):
                value_len = len(str(int(number)))
            else:
                value_len = len(str(float(number)))
            if value_len > max_len:
                max_len = value_len

    # Izveido matricas virknes attēlojumu, kur katra rinda tiek atdalīta ar \n un izlīdzināta atbilstoši maksimālās vērtības garumam
    sv = ""
    for i in range(rindas):
        for j in range(kolonnas):
            number = matrix[i][j]
            if number == 0:
                number = '∙'
            elif number == int(number):
                number = int(number)
            else:
                number = str(float(number))
            atkape = " " * (max_len - len(str(number)))
            sv += atkape + str(number)
            if j < kolonnas - 1 and (j + 1) % 3 != 0:
                sv = sv + " "
            elif j < kolonnas - 1 and (j + 1) % 3 == 0:
                sv = sv + "  "
        sv = sv + "\n"
        if (i + 1) % 3 == 0 and i < rindas - 1:
            sv += "\n"

    return sv


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


a = numpy.zeros((9, 9))

choose = input("Vai gribat nejauši aizpildīt Sudoku spēlēs lapiņu vai manuāli? (n/m) ==> ")
while choose != "n" and choose != "m":
    choose = input("Kļūda! Ievadīet \"n\" vai \"m\"! Vai gribāt nejauši aizpildīt Sudoku kartīti vai manuāli? (n/m) ==> ")

if choose == "n":
    a = fill_array_randomly(9, 9)
    print()
    print(matrix_to_string_float(a))

elif choose == "m":
    b = input_sudoku_matrix()
    print()
    print(matrix_to_string_float(b))

if check_array_rows_and_columns(a) and check_3x3_submatrixes(a):
    print("Ir korekti aizpildīta Sudoku spēlēs lapiņa.")  # VALID
else:
    print("Nav korekti aizpildīta Sudoku spēlēs lapiņa.")  # INVALID


# TESTĒŠANAI
'''
for i in range(1000):
    a = fill_array_randomly(9, 9)
    # Izdrukām masīvu
    print()
    print(matrix_to_string_float(a))
    # if check_array_rows_and_columns(a) and check_3x3_submatrixes(a):
    if check_3x3_submatrixes(a):
        print("VALID")
    else:
        print("INVALID")
'''

# TESTĒŠANAI
'''
for i in range(1000):
    a = fill_array_randomly(9, 9)
    # Izdrukām masīvu
    print()
    print(matrix_to_string_float(a))
    if check_array_rows_and_columns(a):
        print("VALID")
    else:
        print("INVALID")
'''
