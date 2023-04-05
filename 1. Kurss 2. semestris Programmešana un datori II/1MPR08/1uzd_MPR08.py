# Programmas nosaukums: Izveido masīvu ar visiem pirmskaitļiem, kuri ir ne lielāki 10000 un izvada to augošā secībā
# 1. uzdevums (1MPR08_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas izveido visu pirmskaitļu, kas nepārsniedz 10000, augošā secībā sakārtotu masīvu
# un izvada šo masīvu uz ekrāna. Atrast un pielietot formulu, kas nosaka iespējamo pirmskaitļu, kas nepārsniedz patvaļīgu skaitli N,
# skaitu, definējot pirmskaitļu masīva garumu.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


import numpy
import math


def izvade(x):
    # Izvada masīva elementus pēc kārtas līdz pedējam
    # x - viendimensijas masīvs

    try:
        n = len(x)
        s = str(x[0])
        for i in range(1, n):
            s = s + ", " + str(x[i])
        print(s)
    except IndexError:
        print("Nav pirmskaitļu šajā intervālā.")  # Ja parādās index error, tad tas nozīme, ka šajā intervālā nav pirmskaitļu.
    except:
        print("Kļūda!")  # Citām kļūdam


def pirmskaitlu_masivs(n, drosibas_koeficients):
    # Atgriež tuple ar pirmskaitļu masīvu līdz skaitlim n bez liekām 0 un ar nodzēsto nulles skaitu. (Ja ir lieki elementi, tad funkcija to nodzes)
    # n - naturāls skaitlis (int), līdz kurām meklēsīm pirmskaitļus
    # drosibas_koeficients - drošības koeficients. Tiek reizināts ar n/log(n) un tiek izmantots masīva izmēra definēšanai.
    # Parasti, jo lielāks, jo vairāk liekas nulles būs. Pēc noklusējuma labāk, lai tās būtu aptuvēni 1.2

    if n <= 1:  # Funkcija nedarbotos jā ievadīs 0, 1 vai 2, tāpēc tas tiek atsevišķi definēts.
        return numpy.array([])
    if n == 2:
        return numpy.array([2])

    # drosibas_koeficients = 1.2  # izmantots, lai palidzētu nodefinētu masīva izmēru (size). Masīva izmēra definēšanai tiek izmantota formula n/log(n) https://en.wikipedia.org/wiki/Prime_number_theorem un https://en.wikipedia.org/wiki/Prime-counting_function
    size = math.ceil((n / math.log(n)) * drosibas_koeficients)  # aprēķina masīva garumu, izmantojot formulu n/log(n) un reizinot ar drošības koeficientu (bez viņa nevienmēr pietiks vietas)
    p = numpy.zeros(size, dtype=numpy.int32)  # izveido masīvu ar 0 vērtībām tādu garumu, kuru aprēķinaja ar formulu (n/log(n))*drosibas_koeficientu
    p[0] = 2  # pirmais pirmskaitlis
    p[1] = 3  # otrais pirmskaitlis
    j = 2
    k = 5
    try:
        while k <= n:
            i = 0
            s = round(math.sqrt(k))
            while (k % p[i]) != 0:
                i = i + 1
                if p[i] > s:
                    p[j] = k
                    j = j + 1
                    break
            k = k + 2
        deleted_zeros_count = len(p) - len(p[:j])
        return (p[:j], deleted_zeros_count)  # [:j], lai izvadītu bez nullem
    except:
        print("Palieliniet drošības koeficientu! Nepietika vietas masīva aizpildīšanai.")


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


n = 10000  # Līdz kuram skaitlim meklējam pirmskaitļus
drosibas_koeficients = 1.2  # izmantots, lai palidzētu nodefinētu masīva izmēru (size). Masīva izmēra definēšanai tiek izmantota formula n/log(n) https://en.wikipedia.org/wiki/Prime_number_theorem un https://en.wikipedia.org/wiki/Prime-counting_function
print("Pimskaitļi līdz " + str(n) + ":")  # Var mainīt drošības koeficientu, lai mainītu definētā masīva izmēru
pirmskaitli = pirmskaitlu_masivs(n, drosibas_koeficients)
izvade(pirmskaitli[0])
print("Funkcija paredzēja vietas par " + str(pirmskaitli[1]) + " pirmskaitļiem vairāk.")
print(f"{pirmskaitli[1]} liekas nulles masīvā beigās tika nodzestas.")
