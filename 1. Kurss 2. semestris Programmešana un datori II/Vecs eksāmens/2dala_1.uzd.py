'''
def naudasGabali(n):
    # funkcija veic nepieciešamo naudas gabalu aprēķinu
    # nosaka, cik banknotes nepieciešamas
    banknotes = [500, 200, 100, 50, 20, 10, 5]
    v = int(n)  # veselā daļa no ievadītās summas
    for i in range(7):
        while v >= banknotes[i]:
            a = v // banknotes[i]
            v = v - banknotes[i] * a

            print(a, "-", banknotes[i], "euro banknotes")

    # nosaka cik euro monētas nepieciešamas
    monetasEUR = [2, 1]
    for i in range(2):
        while v >= monetasEUR[i]:
            a = v // monetasEUR[i]
            v = v - monetasEUR[i] * a

            print(a, "-", monetasEUR[i], "euro monētas")

    # nosaka cik centu monētas nepieciešamas
    centi = [50, 20, 10, 5, 2, 1]
    l = int(n)  # palīgmainīgais ar sākotnējās summas veselo daļu
    b = round((n - l), 2)
    c = int(b * 100)  # c- centu summa
    for i in range(6):
        while c >= centi[i]:
            a = c // centi[i]
            c = c - centi[i] * a
            print(a, "-", centi[i], "centu monētas")


x = float(input("Ievadiet summu: "))
naudasGabali(x)
'''

# банкноты есть и вот как разделить их на нужные какие выдавать нужно


def bank(summa):
    summa_banknoti = int(summa)
    summa_centi = round((summa - summa_banknoti), 2)
    # print(summa_centi)

    saraksts_banknotu_skaitu = [0, 0, 0, 0, 0, 0, 0]
    banknotes = [500, 200, 100, 50, 20, 10, 5]

    monetas = [2, 1]
    saraksts_monetu_skaitu = [0, 0]

    centi = [50, 20, 10, 5, 2, 1]
    saraksts_centu_skaitu = [0, 0, 0, 0, 0, 0, 0]

    for i in range(len(banknotes)):
        if summa_banknoti >= banknotes[i]:
            saraksts_banknotu_skaitu[i] += 1
            summa_banknoti = summa_banknoti - banknotes[i]

    for i in range(len(monetas)):
        if summa_banknoti >= monetas[i]:
            saraksts_monetu_skaitu[i] += 1
            summa_banknoti = summa_banknoti - monetas[i]

    summa_centi = 100 * summa_centi
    for i in range(len(centi)):
        if summa_centi >= centi[i]:
            saraksts_centu_skaitu[i] += 1
            summa_centi = summa_centi - centi[i]

    for i in range(7):
        if saraksts_banknotu_skaitu[i] == 0:
            pass
        else:
            print(banknotes[i], "EUR banknošu skaits:", saraksts_banknotu_skaitu[i])

    for i in range(2):
        if saraksts_monetu_skaitu[i] == 0:
            pass
        else:
            print(monetas[i], "EUR monetas skaits:", saraksts_monetu_skaitu[i])

    for i in range(7):
        if saraksts_centu_skaitu[i] == 0:
            pass
        else:
            print(centi[i], "euro-centu monetas skaits:", saraksts_centu_skaitu[i])


eur_summa = float(input("Ievadiet EUR summu ==> "))
bank(eur_summa)

'''
def aprēķinaNaudasGabalus(summa):
    # aprēķina nepieciešamo naudas gabalu skaitu
    banknotu_vertibas = [500, 200, 100, 50, 20, 10, 5]

    summa_banknotes = int(summa)
    summa_centi = summa - summa_banknotes

    for i in banknotu_vertibas:
        if summa_banknotes >= banknotu_vertibas[i]:
            skaits = summa_banknotes // summa_banknotes
            summa_banknotes -= summa_banknotes * skaits

            print(f"{skaits} - {banknota} euro banknotes")

    # aprēķina nepieciešamo eiro monētu skaitu
    monētu_vērtības_eiro = [2, 1]

    for monēta in monētu_vērtības_eiro:
        if summa_euro >= monēta:
            skaits = summa_euro // monēta
            summa_euro -= monēta * skaits

            print(f"{skaits} - {monēta} euro monētas")

    # aprēķina nepieciešamo centu monētu skaitu
    monētu_vērtības_centi = [50, 20, 10, 5, 2, 1]
    centu_summa = int((summa - int(summa)) * 100)

    for monēta in monētu_vērtības_centi:
        if centu_summa >= monēta:
            skaits = centu_summa // monēta
            centu_summa -= monēta * skaits

            print(f"{skaits} - {monēta} centu monētas")


ievadītā_summa = float(input("Ievadiet summu: "))
aprēķinaNaudasGabalus(ievadītā_summa)
'''
