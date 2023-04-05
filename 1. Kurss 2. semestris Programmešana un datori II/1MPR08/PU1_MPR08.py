# Programmas nosaukums: Lielo skaitļu dalīšana ar atlikumu
# 1.Papilduzdevums (1MPR08_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas realizē lielo naturālo skaitļu (vismaz ar 50 cipariem) dalīšanas ar atlikumu algoritmu.
# Jāveic ievaddatu korektuma pārbaude!
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


import math


def dalit_lielus_skaitlus(s, n):
    # Funkcija atgriež tuple (dalījums, atlikums) no s / n. Dalījums ir int un atlikums ir int.
    # Jāizmanto lielo skaitļu dalīšanai.
    # Dalā pēc "cipariem".
    # s - str, dalāmais
    # n - str, dalītājs
    n = int(n)
    galva = 0
    atlikums = 0
    dalijums_sv = ""

    for i in range(len(s)):

        cipars = int(s[i])
        tmp = cipars + atlikums * galva
        dalijums_sv = dalijums_sv + str(tmp // n)

        if tmp % n == 0:
            galva = 0
            atlikums = 0
        else:
            atlikums = tmp % n
            galva = 10

    dalijums = nodzest_liekas_nulles(dalijums_sv)
    dalijums = int(dalijums)

    return (dalijums, atlikums)


def nodzest_liekas_nulles(s):
    # Nodzes liekas nulles sākumā
    # s - simbolu virkne
    for i in range(len(s)):
        if s[i] != '0':
            return s[i:]
    return '0'


def is_natural_long(s):
    # Pārbauda vai simbolu virkne reprezentē naturālo skaitli, vai nē.
    # Atgriež True, ja virkne reprezentē naturālo skaitli.
    # Atgriež False, ja nereprezentē naturālo skaitli.
    # s - pārbaudama simbolu virkne

    # Noņema no virknes visas sākuma vai beigu atstarpes
    s = s.strip()

    # Pārbauda, vai virkne ir tukša
    if len(s) == 0 or (len(s) == 1 and s == "0"):
        return False

    # Iet cikliski cauri katrām simbolam simbolu virknē (string'ā)
    for c in s:
        # Ja kāda rakstzīme nav cipars, virkne neatspoguļo naturālu skaitli. return False
        if not c.isdigit():
            return False

    # Virkne atspoguļo naturālu skaitli, ja ietu cauri ciklas netika pamanīts not .isdigit()
    return True


def is_natural_or_zero_long(s):
    # Pārbauda vai simbolu virkne reprezentē naturālo skaitli vai 0, vai nē.
    # Atgriež True, ja virkne reprezentē naturālo skaitli.
    # Atgriež False, ja nereprezentē naturālo skaitli.
    # s - pārbaudama simbolu virkne

    # Noņema no virknes visas sākuma vai beigu atstarpes
    s = s.strip()

    if not s.isdigit():
        return False

    if len(s) == 1 and s == "0":
        return True

    # Iet cikliski cauri katrām simbolam simbolu virknē (string'ā)
    for c in s:
        # Ja kāda rakstzīme nav cipars, virkne neatspoguļo naturālu skaitli. return False
        if not c.isdigit():
            return False

    # Virkne atspoguļo naturālu skaitli, ja ietu cauri ciklas netika pamanīts not .isdigit()
    return True


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


dalamais = input("Ievadiet dalāmo ==> ")
while is_natural_or_zero_long(dalamais) == False:
    dalamais = input("Kļūda! Ievadiet naturālo dalāmo vai nulle ==> ")

dalitajs = input("Ievadiet dalītāju ==> ")
while is_natural_long(dalitajs) == False:
    dalitajs = input("Kļūda! Ievadiet naturālo dalītāju ==> ")

rezultats = dalit_lielus_skaitlus(dalamais, dalitajs)

print("\nNepilnais dalījums:")
print(rezultats[0])
print("\nAtlikums:")
print(rezultats[1])
