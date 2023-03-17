# Programmas nosaukums: Modas noteikšana
# Papilduzdevums 1 (1MPR06_Vladislavs_Babaņins)
# Uzdevuma formulējums: Lietotājs ievada iepriekš zināma garuma nesakārtotu masīvu.
# Noskaidrot un izvadīt uz ekrāna šo skaitļu kopas modu. Ja ir vairākas modas, tad jāpaziņo visas, bet, ja modas nav
# (t.i. visas atšķirīgas vērtības vienādā skaitā), tad jāpaziņo “moda netika atrasta” (2 punkti).
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


import numpy


def is_natural(n):
    # Pārbauda vai simbolu virkne ir naturāls skaitlis vai nav
    # Ja ir naturāls skaitlis, tad True. Ja nav tad False.
    # n - simbolu virkne, kuru pārbauda.
    if str(n).isdigit() and float(n) == int(n) and int(n) > 0:
        return True
    else:
        return False


def izveidot_masivu_ar_garumu(n):
    # Izveido masīvu ar noradīto garumu n
    # n - naturāls skaitlis
    a = numpy.arange(n)
    for i in range(n):
        b = input("Ievadiet " + str(i) + ".elementu ===> ")
        b = is_whole(b, i)
        a[i] = b
    return a


def is_whole(x, i):
    # Pārbauda vai simbolu virkne ir vesels skaitlis un ja nē, tad paprasa ievadīt to vēlreiz (bezgalīgi daudz ievades)
    # Ja simbolu virkne ir vesels skaitlis, tad atgriež to kā int(x)
    # x - pārbaudāma simbolu virkne
    # i - i-tajs elements
    while True:
        try:
            x = int(x)
        except:
            x = input("Kļūda! Ievadiet " + str(i) + ".elementu ===> ")
        else:
            return int(x)


def izvade(x):
    # Izvada masīva elementus pēc kārtas līdz pēdējam
    # x - viendimensijas masīvs
    n = len(x)
    s = str(x[0])
    for i in range(1, n):
        s = s + ", " + str(x[i])
    print(s)


def mode(masivs):
    # Atrod masīva modu un atgriež masīvu ar modam (vai modu)
    # Ja masīva visi elementi ir vienādi, tad atgriež False (moda netika atrasta)
    # masivs - viendimensijas masīvs (kurš vel netika kārtots augoša secība)
    '''
    Paskaidrojums, kā šī funkcija darbojas:

    Funkcija vispirms paņem, ka moda ir pirmais sakārtotā masīva elements.
    Pēc tam, funkcija iziet cauri katram masīva elementam un atjaunina sarakstu ar modam un to biežumu katru reizi, kad tiek atrasta jauna mode ar augstāku biežumu (elements, kuru ir vairāk).
    Ja tas saskaras ar modu ar tādu pašu biežumu (biežums - skaits, cik reizes paradās šis elements) kā pašreizēja moda, tad tas pievieno jauno modu, modu sarakstam.

    Funkcija iterē katru elementu sakārtotajā masīvā un pārbauda, vai tas ir vienāds ar iepriekšējo elementu.
    Ja tā ir, mainīgais "sk" tiek palielināts. Ja tā nav, funkcija pārbauda, vai pašreizējais skaits ir lielāks par līdz šim saglabāto maksimālo skaitu.
    Ja ir lielāks, tad maksimālais skaits tiek atjaunināts un pašreizējais skaitlis (elements) tiek pievienots modas sarakstam.
    Ja pašreizējais skaits ir vienāds ar maksimālo līdz šim saglabāto skaitu, modas sarakstam tiek pievienots arī šis skaitlis (elements) (vairākas modes).
    Pēc tam kad tika "iziterēts" viss masīvs, tad pārbaudām, vai pēdējā elementa biežums ir lielāks par līdz šim redzēto maksimālo biežumu. 
    Ja tā ir, tad maksimālais skaits tiek atjaunināts un modas saraksts ir tas pēdējais elements. 
    Ja pēdējā elementa skaits ir vienāds ar maksimālo līdz šim redzēto (saglabāto) skaitu, modas sarakstam tiek pievienots arī pēdējais elements (vairākas modes).

    Ja maksimālais biežums ir vienāds ar 1 (t.i., visi masīva elementi ir unikāli), funkcija atgriež vērtību False. 
    Pretējā gadījumā tas atgriež atrasto modas sarakstu.
    '''

    sort_atrais_augosa(masivs, 0, len(masivs) - 1)  # Ievadītais masīvs tiek izkārtots augošā secībā, izmantojot sort_atrais_augosa
    sk = 1  # seko pašreizējā apstrādājamā skaitļa (elementa) biežumam
    max_sk = 1  # saglabā jebkura masīva skaitļa (elementa) maksimālo biežumu
    modas_list = [masivs[0]]  # līdz šim atrasto modu saraksts

    if len(masivs) == 1:  # Ja masīva garums ir 1, tad moda arī ir tas skaitlis (vienīgais elements)
        modas_list = [masivs[0]]
        return modas_list

    for i in range(1, len(masivs)):
        if masivs[i] == masivs[i - 1]:  # Ja elements i ir vienāds ir i - 1, tad palielinām skaitītāju
            sk = sk + 1
        else:
            if sk > max_sk:  # ja skaititajs kļūst lielāks nekā maksimālais skaitītājs
                max_sk = sk  # tad maksimālais skaititajs atjaunojas
                modas_list = [masivs[i - 1]]  # modas saraksts atjaunojas un paliek tas masīva elements, kurš vislielāko reizi paradījās pēc skaitītajā

            elif sk == max_sk:  # Ja skaititajs ir vienāds ar pašreizējo maksimālo skaitītāju (max biežumu)
                modas_list.append(masivs[i - 1])  # tad pievienojam sarakstam jauno modu (papildus modu)

            sk = 1  # pēc iterācijām sk atkal kļūst par 1

    if sk > max_sk:  # Tas ir veidots pēdējam elementam. Ja lielāks skaititajs nekā pašreizējais maksimālais.
        max_sk = sk  # tad atjaunojam maksimālo skaitītāju
        modas_list = [masivs[-1]]  # atjaunojam modas sarakstu

    elif sk == max_sk:  # Ja modas biežumi ir vienādi, tad pievienojam modas sarakstam
        modas_list.append(masivs[-1])

    if max_sk == 1:  # Ja maksimālais biežums ir vienāds ar 1 (visi masīva elementi ir unikāli), atgriež vērtību False
        return False
    else:
        return modas_list  # Atgriež atrasto modas sarakstu


def sort_atrais_augosa(a, sv, bv):
    # Sakārto masīvu augoša secība un atgriež salīdzināšanas skaitu, lai sakārtotu masīvu
    # Kārtošanas tiek izmantota Hoara (ātrais) metode (quicksort)
    # a - viendimensijas masīvs
    # sv - sākuma vērtība
    # bv - beigu vērtība
    if sv < bv:
        i = sv
        j = bv
        solis = -1
        lv = True
        while i != j:
            if lv == (a[i] > a[j]):
                x = a[i]
                a[i] = a[j]
                a[j] = x
                x = i
                i = j
                j = x
                lv = not lv
                solis = -solis
            j = j + solis
        sort_atrais_augosa(a, sv, i - 1)
        sort_atrais_augosa(a, i + 1, bv)


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


m = input("Ievadiet masīva izmēru N ===> ")

while is_natural(m) == False:
    m = input("Masīva izmērs ir naturāls skaitlis!\nIevadiet masīva izmēru N ===> ")

m = int(m)

print("Ievadiet masīva skaitļus!")
t = izveidot_masivu_ar_garumu(m)

print("\nIevadīta skaitļu kopa:")
izvade(t)

sort_atrais_augosa(t, 0, len(t) - 1)
print("\nSakārtota skaitļu kopa:")
izvade(t)

modas = mode(t)

if modas == False:
    print("\nModa netika atrasta.")
else:
    print("\nSkaitļu kopas moda(s) ir:")
    izvade(modas)
