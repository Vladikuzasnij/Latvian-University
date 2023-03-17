# Programmas nosaukums: Vienādojuma ax3+by2+cz+d=0 atrisināšana
# 2. uzdevums (1MPR01_Vladislavs_Babaņins)
# Uzrakstīt programmu, kas atrod vienādojuma ax3+by2+cz+d=0 visus atrisinājumus veselos skaitļos intervālā no -10 līdz 10
# (abus galapunktus ieskaitot), koeficientus a, b, c un d ievada no tastatūras
# Programmas autors: Vladislavs Babaņins
# Versija 1.0

def solve_equation_ax3_plus_by2_plus_cz_plus_d_equals_0(a, b, c, d):
    # Funkcija atrod visus veselos atrisinājumus vienādojumam ax^3 + by^2 + cz + d = 0
    # Funkcija izmanto pilno pārlasi. Tālak funkcija nodot "kortežus" (x, y, z) veidā kā vienu lielo simbolu virkni
    # a - funkcijas parametrs a (ax^3 + ...)
    # b - funkcijas parametrs b (... + by^2 + ...)
    # c - funkcijas parametrs c (... + cz + ...)
    # d - funkcijas parametrs d (... + d = 0)
    sv = ""
    for x in range(-10, 11):
        for y in range(-10, 11):
            for z in range(-10, 11):
                if a * x * x * x + b * y * y + c * z + d == 0:
                    sv += "(" + str(x) + ", " + str(y) + ", " + str(z) + ")\n"
    return sv


def is_real(n):
    # Pārbauda vai simbolu virkne ir reāls (racionāls) skaitlis vai nav
    # Ja ir reāls skaitlis, tad True. Ja nav tad False.
    # n - simbolu virkne, kuru pārbauda.
    try:
        n = float(n)
    except:
        return False
    else:
        return True

# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


a = input("Ievadiet koeficientu a ==> ")

while is_real(a) == False:
    a = input("Kļūda! a nav reāls skaitlis.\nIevadiet koeficientu a ==> ")

b = input("Ievadiet koeficientu b ==> ")

while is_real(b) == False:
    b = input("Kļūda! b nav reāls skaitlis.\nIevadiet koeficientu b ==> ")

c = input("Ievadiet koeficientu c ==> ")

while is_real(c) == False:
    c = input("Kļūda! c nav reāls skaitlis.\nAIevadiet koeficientu c ==> ")

d = input("Ievadiet koeficientu d ==> ")

while is_real(d) == False:
    d = input("Kļūda! d nav reāls skaitlis.\nIevadiet koeficientu d ==> ")

a = float(a)
b = float(b)
c = float(c)
d = float(d)

sv = solve_equation_ax3_plus_by2_plus_cz_plus_d_equals_0(a, b, c, d)

if sv == "":
    print("\nVienādojumam " + str(a) + "*x^3 + " + str(b) + "*y^2 + " + str(c) + "*z + " + str(d) + " = 0 nav atrisinājumus veseļos skaitļos intervāla [-10;10]")
else:
    print("\nVienādojuma " + str(a) + "*x^3 + " + str(b) + "*y^2 + " + str(c) + "*z + " + str(d) + " = 0 atrisinājumi veseļos skaitļos intervāla [-10;10] ir sekojoši skaitļu korteži (x,y,z): \n")

# Izvadām risinājuma "kortežus" (x, y, z) veidā.
print(sv)
