# Programmas nosaukums: Lielo skaitļu kvadrātsaknes izvilkšanas algoritms
# 2.Papilduzdevums (1MPR08_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas realizē kvadrātsaknes izvilkšanas algoritmu lielajiem naturālajiem skaitļiem (vismaz ar 50 cipariem) ar precizitāti līdz veselam skaitlim.
# Jāveic ievaddatu korektuma pārbaude!
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


# import math  # Testēšanai


def long_sqrt(skaitlis):
    # Funkciju, kas kā ievadi izmanto nenegatīvu veselu skaitli un atgriež tā veselā skaitļa kvadrātsakni
    # skaitlis - int, skaitlis, no kura vajag atrast kvadrātsakni
    # Atgriež sqrt(skaitlis) kā int

    # Konvertējat ievadīto veselo nenegatīvo skaitli par simbolu virkni un saglabājam to mainīgajā
    sk_sv = str(skaitlis)  # sk_sv - skaitlis_simbolu virkne
    # Saglabājam ievadītā veselā skaitļa simbolu virknes garumu
    len_sk = len(sk_sv)  # slen_skaitlis

    # Ja ievadītā veselā skaitļa simbolu virknes garums ir nepāra skaitlis, tad pievienojam sākuma nulli, lai padarītu to par pāru simbolu virkni (garums ir pāra skaitlis)
    if len_sk % 2 == 1:
        sk_sv = '0' + sk_sv  # Ievadītā veselā skaitļa simbolu virknei sākumam pievienojam '0'
        len_sk = len_sk + 1  # Palielinām ievadītā veselā skaitļa simbolu virknes garumu par 1

    result = ''  # Tukša simbolu virkne, lai saglabātu kvadrātsaknes aprēķina rezultātu
    atlikums = 0

    # Sadalām ievadītā veselā skaitļa virknes pirmos divus ciparus [:2]
    a = int(sk_sv[:2])

    j = 1              # Atrodam pirmo "tuvinājumu"
    while j * j <= a:  # Tas ir lai atrastu pirmo ciparu kvadrātsaknei
        j = j + 1      # Var arī atrast tā:
    sakne = j - 1      # sakne = int(a**0.5) (lai nebūtu cikls)

    result = result + str(sakne)
    atlikums = a - sakne * sakne  # Atlikums
    # Cikls pār katru otro "ciparu pāri"
    for i in range(2, len_sk, 2):  # Stabiņveidā atrodam nākamo un nākamo un ... un pēdējo ciparu
        # Reizinām atlikumu ar 100 un pievienojiet nākamos divus veselā skaitļa ciparus, lai iegūtu dividendi
        a = atlikums * 100 + int(sk_sv[i:i + 2])
        cipars = 0
        temp = sakne * 20
        while (temp + cipars) * cipars <= a:
            cipars += 1
        cipars -= 1
        result += str(cipars)  # Rezultātam pievienojam iegūto ciparu
        atlikums = a - (temp + cipars) * cipars
        sakne = sakne * 10 + cipars

    return int(result)


def is_natural_or_zero_long(s):
    # Pārbauda vai simbolu virkne reprezentē naturālo skaitli vai 0, vai nē.
    # Atgriež True, ja virkne reprezentē naturālo skaitli.
    # Atgriež False, ja nereprezentē naturālo skaitli.
    # s - pārbaudāma simbolu virkne

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


n = input("Ievadiet naturālo skaitli vai 0 kvadrātsaknes vilkšanai ==> ")
while is_natural_or_zero_long(n) == False:
    n = input("Kļūda! Ievadiet naturālo skaitli vai 0 kvadrātsaknes vilkšanai ==> ")
n = int(n)

print("\nsqrt(" + str(n) + ")")
print("≈")
print(long_sqrt(n))
# math.sqrt(skaitlis) # Testēšanai

# Testēšanai
'''
for i in range(1, 10000000, 1):  # for i in range(1, 1000000, 1):
    print("sqrt(" + str(i) + ") =", math.floor(math.sqrt(i)))
    print(str(long_sqrt(i)) + " == " + str(math.floor(math.sqrt(i))))
    if long_sqrt(i) == math.floor(math.sqrt(i)):
        print("TRUE\n")
    else:
        print("FALSE\n")
'''
