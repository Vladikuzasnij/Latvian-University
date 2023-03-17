# Programmas nosaukums: punkta koordinātu XX un YY vērtības
# 1. uzdevums (1MPR04_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas nosaka punkta koordinātu XX un YY vērtības, ja riņķa rādiusu R un punkta koordinātas X un Y ievada lietotājs no tastatūras.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


import math


def is_real_positive(n):
    # Pārbauda vai simbolu virkne ir reāla pozitīva vērtība
    # Ja ir tad return True
    # Ja nav tad return False
    # vai n >= 0
    # n - simbolu virkne (str)
    try:
        n = float(n)
        b = math.sqrt(n)
        c = 1 / n
    except:
        return False
    else:
        return True


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


def is_real_not_negative(n):
    # Pārbauda vai simbolu virkne n ir reāls nenegatīvs skaitlis vai nē
    # Ja ir, tad return True
    # Ja nē, tad return False
    try:
        n = float(n)
        b = math.sqrt(n)
    except:
        return False
    else:
        return True


def krustpunkts(punkts, radius):
    # Atrod nepieciešāmo krustpunktu un return kā kortežu (xx, yy)
    # punkts - (x1,y1) kortežs
    # radius - rādiusa vērtība [0; + bezg)
    (x, y) = punkts
    if (x, y) == (0, 0) and radius == 0:
        return False # Dalīšana ar 0
    d = math.sqrt(x * x + y * y)
    xx = x * radius / d
    yy = y * radius / d
    return (xx, yy)


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


x1 = is_real_number_velreiz("X")
y1 = is_real_number_velreiz("Y") # float(input("Ievadiet Y ===> "))
p1 = (x1, y1)

radius = is_real_number_velreiz("R")# input("Ievadiet rādiusu ===> ")

while not is_real_not_negative(radius):
    radius = float(input("Kļūda! Rādiusam ir jābut reālai nenegatīvai vērtībai!\nIevadiet rādiusu ===> "))

radius = float(radius)

if krustpunkts(p1, radius) == False:
    print("Šajā gadījumā nevar viennozīmīgi noteikt atbildi.") #if p1 == (0, 0) and radius == 0:
else:
    print("(XX,YY) = " + str(krustpunkts(p1, radius)))
