# Programmas nosaukums: Labirints ar necaurejami šķēršļiem.
# 3. uzdevums (1MPR09_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas realizē labirinta izveidi un apstaigāšanu atbilstoši lekcijā dotajiem nosacījumiem,
# papildus paredzot, ka labirinta 5% no rūtiņu kopskaita ir necaurejami šķēršļi.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


import numpy


def is_labirint_path(i, j, lab, tr):
    # Atgriež masīvu found_path (atrasts ceļš), kurš sastāv no frāzem "Pa labi", "Uz leju".
    # Rekursīvi atrod ceļu, lai izietu no labirinta (var iet tikai no mazākas vērtības uz lielāku (vai vienādu)).
    # i - 0 (parasti)
    # j - 0 (parasti)
    # lab - divdimensijas masīvs ar labirinta segmēnta vērtībam.
    # tr - trase
    # trase = numpy.empty(path_length, "O")
    # path_length = n + m - 2

    n = lab.shape[0] - 1
    m = lab.shape[1] - 1

    if (i == n) and (j == m):
        return True
    else:
        found_path = False
        if (i < n) and (lab[i + 1, j] >= lab[i, j]):
            tr[i + j] = "Uz leju"
            found_path = is_labirint_path(i + 1, j, lab, tr)
        if not found_path and (j < m) and (lab[i, j + 1] >= lab[i, j]):
            tr[i + j] = "Pa labi"
            found_path = is_labirint_path(i, j + 1, lab, tr)
        return found_path


def izvade(a):
    # Atgriež simbolu virkni, kura reprezentē noteikto matricu, kā simbolu virkni stābiņveidā.
    # -1 pārkonvertē kā X.
    # X - nejauši šķēršļi (-1)
    # a - divdimensijas masīvs (matrica)

    # a.ndim # dimensiju skaits
    # a.shape # kortežs ar masīva izmēriem

    n = a.shape[0]  # x axis
    m = a.shape[1]  # y axis
    s = "\n"
    for i in range(n):
        for j in range(m):
            if a[i, j] == -1:
                s = s + "   X"
            else:
                s = s + "{:4d}".format(int((a[i, j])))
        s = s + "\n"
    return s


def get_column(a):
    # a - viendimensijas masīvs
    # [1, 2, 3] konvertēsies
    # 1
    # 2
    # 3
    # Atgriež str masīva elementus, kā kolonnu

    col_str = ""
    for elem in a:
        col_str = col_str + str(elem) + "\n"
    return col_str


def random_negative_fill(a, chance):
    # chance = 0.05 (5%) no kopēja skaita būs šķēršļi (-1)
    # chance - skaitlis (float). Jo lielāka šī vērtība, jo lielāka iespēja, ka būs vairāk "segmēntu" ar -1.
    # a - divdimensijas masīvs (labirints)
    # Atgriež divdimensijas masīvu (matricu) kurš ir aizpildīts ar -1.
    # -1 skaits ir chance * masīva_kopējais_elementu_skaits (chance == 0.05 (5%))

    a_shape = a.shape

    # Aprēķinat ievietojamo negatīvo vērtību skaitu
    num_negatives = int(a_shape[0] * a_shape[1] * chance)

    # Izvēlieties nejaušus rindu un kolonnu "segmēntus", lai ievietotu negatīvas vērtības
    indices = numpy.zeros((num_negatives, 2), dtype=int)  # indices ir nulles masīvs, kura izmērs ir (num_negatives, 2), un tajā tiek glabāti izvēlēto "segmētu" rindu un kolonnu koordinātas.
    # Pēc nejauši izvēlēto koordinātu noteikšanas row_idx un col_idx, tiek pārbaudīts, vai tās nav jau aizpildītas ar -1, un
    # vai tās nav sākumpunkts (0, 0) vai beigu punkts (a_shape[0] - 1, a_shape[1] - 1), kas atbilst labirinta sākumam un beigām.
    # Ja nosacījumi tiek izpildīti, koordinātas tiek ievietotas masīvā indices un while cikls tiek pārtraukts.
    for i in range(num_negatives):
        while True:  # Tiek izmantots while cikls, lai izvēlētos "segmētu" koordinātas, kas nav jau iepriekš aizpildītas ar -1.
            row_idx = numpy.random.randint(a_shape[0])
            col_idx = numpy.random.randint(a_shape[1])
            if a[row_idx, col_idx] != -1 and not (row_idx == 0 and col_idx == 0) and not (row_idx == a_shape[0] - 1 and col_idx == a_shape[1] - 1):
                indices[i] = (row_idx, col_idx)
                break

    # Aizpildit nejauši izvēlētus "segmēntus" ar -1

    row_indices = indices[:, 0]
    col_indices = indices[:, 1]

    for i in range(len(row_indices)):
        row_idx = row_indices[i]
        col_idx = col_indices[i]
        a[row_idx, col_idx] = -1

    return a


def is_natural(n):
    # Pārbauda vai simbolu virkne ir naturāls skaitlis vai nav
    # Ja ir naturāls skaitlis, tad True. Ja nav tad False.
    # n - simbolu virkne, kuru pārbauda.
    if str(n).isdigit() and float(n) == int(n) and int(n) > 0:
        return True
    else:
        return False


def is_natural_or_zero(n):
    # Pārbauda vai simbolu virkne ir naturāls skaitlis vai nulle, vai nav
    # Ja ir naturāls skaitlis vai nulle, tad True. Ja nav tad False.
    # n - simbolu virkne, kuru pārbauda.
    if str(n).isdigit() and float(n) == int(n) and int(n) >= 0:
        return True
    else:
        return False


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


n = input("Ievadi labirinta garumu ===> ")
while not is_natural(n):
    n = input("Kļūda! Ievadiet naturālu labirinta garumu ==> ")
n = int(n)

m = input("Ievadi labirinta platumu ===> ")
while not is_natural(m):
    m = input("Kļūda! Ievadiet naturālu labirinta platumu ==> ")
m = int(m)


labirints = numpy.empty((n, m))
path_length = n + m - 2
trase = numpy.empty(path_length, "O")


for i in range(n):
    for j in range(m):
        t = input("Labirints(" + str(i) + "," + str(j) + ") ===> ")
        while not is_natural_or_zero(t):
            t = input("Kļūda! Ievadiet naturālu (vai 0) labirinta segmēnta vērtību!\nLabirints(" + str(i) + "," + str(j) + ") ===> ")
        labirints[i, j] = t

print("\nJusu labirints:")
print(izvade(labirints))

print("Jusu labirints ar nejaušiem šķēršļiem (5% no kopēja skaita):")
a = random_negative_fill(labirints, 0.05)
print(izvade(a))

if is_labirint_path(0, 0, a, trase):
    print("Labirintā var virzoties tikai no mazākas vērtības uz lielāku (vai vienādu)!\nVirzoties var tikai uz leju vai pa labi!")
    print("Labirintu var iziet virzoties tā:")
    print(get_column(trase))

else:
    print("Labirints nav izejams!")
