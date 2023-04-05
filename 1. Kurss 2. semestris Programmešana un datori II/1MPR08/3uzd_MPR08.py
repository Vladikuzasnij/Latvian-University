# Programmas nosaukums: Lielo skaitļu atņemšana
# 3. uzdevums (1MPR08_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas realizē lielo naturālo skaitļu (vismaz ar 50 cipariem) atņemšanu.
# Pirms darbības veikšanas jāpārliecinās, ka mazināmai ir lielāks nekā mazinātājs.
# Jāveic ievaddatu korektuma pārbaude!
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


import numpy


def izvade_bez_komatiem_kopigi(x):
    # Izvada masīva elementus pēc kārtas līdz pedējam kopīgi bez komatiem (izmanto lai izvadītu masīvu kā vienu str skaitli)
    # x - viendimensijas masīvs
    n = len(x)
    s = str(x[0])
    for i in range(1, n):
        s = s + "" + str(x[i])
    print(s)


def parveide_sv_to_mas(sv, m):
    # Transformē simbolu virkni masīvā ar noradīto garumu. Ja garums ir lielāks nekā simbolu virkne, tad beigās tiek pieliktas 0
    # sv - simbolu virkne, kura sastāv no cipariem
    # m - garums, līdz kurām vajag transformēt simbolu virkni sarakstā. Ja garums ir lielāks nekā simbolu virkne, tad beigās tiek pieliktas 0
    n = len(sv)
    a = numpy.arange(m)
    for i in range(n):
        a[i] = int(sv[-i - 1])
    for i in range(n, m):
        a[i] = 0
    return a[::-1]


def parveide_mas_to_sv(a):
    # Transformē masīvu simbolu virknē. Ja masīvā priekšā ir 0, tad tas tiek noņemtas
    # a - viendimensijas masīvs
    n = len(a)
    sv = ""
    for i in range(n):
        sv = str(a[i]) + sv
    return sv


def parveide_mas_to_sv_reverse(a):
    # Transformē masīvu simbolu virknē un apgriež to
    # a - viendimensijas masīvs
    n = len(a)
    sv = ""
    for i in range(n):
        sv = str(a[i]) + sv
    return sv[::-1]


def remove_front_zeros(s):
    # Atgriež simbolu virkni bez nullem priekšā
    # s - simbolu virkne, kura sastav no cipariem, potenciāli ar nullēm priekšā
    i = 0
    while i < len(s) - 1 and s[i] == '0':
        i += 1
    s = s[i:]
    return s


def atnemsana(a, b):
    # Atņem masīvu a no b izmantojot str. Jāizmanto lielo skaitļu (vismaz ar 50 cipariem) atņemšanai. Atgriež simbolu virkni bez nullem priekšā
    # a - viendimensijas masīvs
    # b - viendimensijas masīvs
    if str(a) == str(b):
        return "0"

    n1 = len(a)
    n2 = len(b)
    if n1 > n2:
        n = n1
    else:
        n = n2
    m1 = parveide_sv_to_mas(a, n)
    m2 = parveide_sv_to_mas(b, n)
    m3 = numpy.zeros(n, dtype=numpy.int_)

    for i in range(-1, -n1, -1):
        if m1[i] < m2[i]:
            m1[i - 1] = m1[i - 1] - 1
            m1[i] = m1[i] + 10

    for i in range(n):
        m3[i] = m1[i] - m2[i]

    a = parveide_mas_to_sv(m3)
    a = a[::-1]
    a = remove_front_zeros(a)
    return a


def is_natural_or_zero_long(s):
    # Pārbauda vai simbolu virkne reprezentē naturālo skaitli vai 0, vai nē.
    # Atgriež True, ja virkne reprezentē naturālo skaitli.
    # Atgriež False, ja nereprezentē naturālo skaitli.
    # s - pārbaudāma simbolu virkne

    # Noņema no virknes visas sākuma vai beigu atstarpes
    s = s.strip()

    # Pārbauda, vai virkne ir tukša
    if len(s) == 0:
        return False

    # Iet cikliski cauri katrām simbolam simbolu virknē (string'ā)
    for c in s:
        # Ja kāda rakstzīme nav cipars, virkne neatspoguļo naturālu skaitli. return False
        if not c.isdigit():
            return False

    # Virkne atspoguļo naturālu skaitli, ja ietu cauri ciklas netika pamanīts not .isdigit()
    return True


def is_a_bigger_b(a, b):
    # Vai masīvs a ir lielāks vai vienāds nekā masīvs b, ja jā, tad return True. Ja nē, tad return False
    # a - pirmais viendimensijas masīvs
    # b - otrais viendimensijas masīvs
    a = parveide_mas_to_sv_reverse(a)
    b = parveide_mas_to_sv_reverse(b)
    if int(a) < int(b):
        return False
    else:
        return True


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


a = input("Ievadiet mazināmo ===> ")
while is_natural_or_zero_long(a) == False:
    a = input("Kļūda! Skaitļa izmēram jābūt naturālam skaitlim vai nulle!\nIevadiet mazināmo ===> ")

a = parveide_sv_to_mas(a, len(a))


b = input("Ievadiet mazinātāju ===> ")
while is_natural_or_zero_long(b) == False:
    b = input("Kļūda! Skaitļa izmēram jābūt naturālam skaitlim vai nulle!\nIevadiet mazinātāju ===> ")

b = parveide_sv_to_mas(b, len(b))


if is_a_bigger_b(a, b) == False:
    print("Kļūda! Mazināmam jābūt lielākam par mazinātāju!")
else:
    print("")
    izvade_bez_komatiem_kopigi(a)
    print("-")
    izvade_bez_komatiem_kopigi(b)
    print("=")
    print(atnemsana(a, b))
