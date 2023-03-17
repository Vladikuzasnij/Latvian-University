# Programmas nosaukums: Noskaidro vai šīs taisnes krustojas tā, lai izveidotos trijstūris.
# 2. uzdevums (1MPR04_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas noskaidro vai šīs taisnes krustojas tā, lai izveidotos trijstūris. Koeficientus a_{11},\ a_{12},\ a_{13},\ a_{21},\ a_{22},\ a_{23},\ a_{31},\ a_{32},\ a_{33} ievada no tastatūras. Ja taisnes krustojoties veido trijstūri, tad aprēķināt tā laukumu.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


import math


def det(a, b, c, d):
    # Atgriež determinanta vērtību
    # a - skaitlis float
    # b - skaitlis float
    # c - skaitlis float
    # d - skaitlis float
    return a * d - b * c


def mala(kp1, kp2): # kp1 = (a,b)   kp2 = (c,d)
    # Malas garums pēc diviem punktiem
    # Atgriež malas garumu
    # kp1 - 1. punkts
    # kp2 - 2. punkts
    return math.sqrt((kp1[0] - kp2[0]) * (kp1[0] - kp2[0]) + (kp1[1] - kp2[1]) * (kp1[1] - kp2[1]))


def laukums(kp1, kp2, kp3): # kp1 =(a,b)   kp2 = (c,d)   kp3 = (f,g)
    # Noskaidro trījstūra laukumu ar Herona formulu pēc trīs krustpunktiem
    # kp1 - 1. krustpunkts
    # kp2 - 2. krustpunkts
    # kp3 - 3. krustpunkts
    m1 = mala(kp1, kp2)
    m2 = mala(kp1, kp3)
    m3 = mala(kp2, kp3)

    p = (m1 + m2 + m3) / 2

    return math.sqrt(p * (p - m1) * (p - m2) * (p - m3))


def vai_pa_pariem_krustojas(t1, t2, t3):
    # Funkcija noskaidro vai pa pariem krustojas trīs taisnes
    # return True, ja krustojas
    # return False, ja nekrustojas
    # t1 - pirmā taisne
    # t2 - otrā taisne
    # t3 - treša taisne
    if (det(t1[0], t1[1], t2[0], t2[1]) * det(t1[0], t1[1], t3[0], t3[1]) * det(t2[0], t2[1], t3[0], t3[1])) == 0:
        return False
    else:
        return True


def krustpunkts(t1, t2):
    # t1 - pirmā taisne
    # t2 - otrā taisne
    # return krustpunktu divām taisnēm (x,y)
    d = det(t1[0], t1[1], t2[0], t2[1])
    dx = det(t1[1], t1[2], t2[1], t2[2])
    dy = det(t1[2], t1[0], t2[2], t2[0])

    x = dx / d
    y = dy / d
    return (x, y)


def is_real_number_velreiz(X): # Bezgalīgi daudz reizes ievāda
    # Prasa ievadīt "X" skaitli un pārbauda, vai tas ir reāls skaitlis vai nav
    # Ja tas ir reāls skaitlis tad atdot float(x1) ievadīto
    # X - ievada ka str vērtību, atspoguļojas tikai kosmetiski (Ievaditet "X" vērtību)
    x1 = input("Ievadiet " + X + " ===> ")
    while True:
        try:
            x1 = float(x1)
        except:
            x1 = input("Kļūda! " + X + " ir jābut skaitlim!\nIevadiet " + X + " ===> ")
        else:
            return float(x1)


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


a11 = is_real_number_velreiz("a11")
a12 = is_real_number_velreiz("a12")
a13 = is_real_number_velreiz("a13")
t1 = (a11, a12, a13)

a21 = is_real_number_velreiz("a21")
a22 = is_real_number_velreiz("a22")
a23 = is_real_number_velreiz("a23")
t2 = (a21, a22, a23)

a31 = is_real_number_velreiz("a31")
a32 = is_real_number_velreiz("a32")
a33 = is_real_number_velreiz("a33")
t3 = (a31, a32, a33)


if vai_pa_pariem_krustojas(t1, t2, t3):
    kp1 = krustpunkts(t1, t2)
    kp2 = krustpunkts(t1, t3)
    kp3 = krustpunkts(t2, t3)
    s = laukums(kp1, kp2, kp3)
    if s != 0:
        print("Taisnes krustojas, ierobežojot laukumu S = " + str(s))
    else:
        print("Taisnes krustojas vienā punktā. Trijsturūris neveidojas.")
else:
    print("Taisnes nekrustojas")
