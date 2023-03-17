# Programmas nosaukums: Noteiktas izteiksmes vērtība
# 4. uzdevums (1MPR01_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas noskaidro, no kādiem pirmskaitļiem var izveidot četrus lietotāja
# patvaļīgi ievadītos naturālos skaitļus (skaitļus veido tikai kā pirmskaitļu reizinājumu,
# piemēram, 100=2*2*5*5). Pirmskaitļi ir jāpaziņo augošā secībā.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0

def is_natural(n):
    # Pārbauda vai simbolu virkne ir naturāls skaitlis vai nav
    # Ja ir naturāls skaitlis, tad True. Ja nav tad False.
    # n - simbolu virkne, kuru pārbauda.
    if str(n).isdigit() and float(n) == int(n) and int(n) > 0:
        return True
    else:
        return False


def sadalisana_uz_pirmskaitliem_kuri_neatkartojas(x):
    # Sadala skaitli x uz pirmskaitliem, kuri neatkartojas
    # Ja ir naturāls skaitlis, tad True. Ja nav tad False.
    # x - naturāls skaitlis
    n = 2
    r = ""
    while x > 1:
        if x % n == 0:
            r = r + str(n) + " "
            x = x // n
            while x % n == 0:
                x = x // n
        n += 1

    if r == "":
        return 1
    return r

# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


a = input("Ievadiet pirmo skaitli ==> ")
while is_natural(a) == False:
    a = input("Kļūda! Pirmais skaitlis nav reāls skaitlis.\nIevadiet pirmo skaitli ==> ")

b = input("Ievadiet otro skaitli ==> ")
while is_natural(b) == False:
    b = input("Kļūda! Otrais skaitlis nav reāls skaitlis.\nIevadiet otro skaitli ==> ")

c = input("Ievadiet trešo skaitli ==> ")
while is_natural(c) == False:
    c = input("Kļūda! Trešais skaitlis nav reāls skaitlis.\nIevadiet trešo skaitli ==> ")

d = input("Ievadiet ceturto skaitli ==> ")
while is_natural(d) == False:
    d = input("Kļūda! Ceturtais skaitlis nav reāls skaitlis.\nIevadiet ceturto skaitli ==> ")

a = int(a)
b = int(b)
c = int(c)
d = int(d)

x = a * b * c * d

result = sadalisana_uz_pirmskaitliem_kuri_neatkartojas(x)

print("Ievadītos skaitļus var izveidot no šādiem pirmskaitļiem: " + str(result))
