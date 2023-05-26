# Programmas nosaukums: Latiņu alfabētu burtu biežums tekstā
# 1. uzdevums (1MPR15_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas skaita, cik un kādi latīņu alfabēta burti (lielie un mazie burti netiek šķiroti) satur dotais teksts.
# Rezultātu uz ekrāna izvada burtu biežuma dilstošā secībā.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


import math


class SymbolCount:
    def __init__(self, burts, skaits):
        # Inicializācija.
        # Instancei ir burts un skaits vērtības.
        # Strāda lidzīgi kortēžam ("burts", skaits), piemēram ("A", 0).

        self.burts = burts
        self.skaits = skaits

    def __repr__(self):
        # Izvada lietotājam instances burtu un skaitu, izmantojot print.
        # Piemēram:
        # print(alphabet[0])
        # Izvada:
        # ("A", 24422)

        return f'("{self.burts}", {self.skaits})'

    @staticmethod
    def create_latin_alphabet():
        # Atgriež sarakstu ar lieliem latiņu alfabētu burtiem alfabētiska secība, kur katram burtam ir piekārtots skaits 0.
        # Lidzīgi kā atgriež tādu sarakstu ar kortežiem:
        # [("A", 0), ("B", 0), ("C", 0), ("D", 0), ("E", 0), ("F", 0), ("G", 0), ("H", 0), ("I", 0), ("J", 0), ("K", 0), ("L", 0), ("M", 0), ("N", 0), ("O", 0), ("P", 0), ("Q", 0), ("R", 0), ("S", 0), ("T", 0), ("U", 0), ("V", 0), ("W", 0), ("X", 0), ("Y", 0), ("Z", 0)]
        # Izmanto chr funkciju.

        saraksts = []
        for i in range(26):
            burts = chr(i + 65)
            skaits = 0
            saraksts.append(SymbolCount(burts, skaits))

        return saraksts

    @staticmethod
    def update_symbol_count(alphabet, symbol):
        # Atjauno (palielinā par vienu) simbolu (burtu) skaitu alphabet mainīgajā, konkrētāja vietā (kur ir tās noteikts kortežs ar atbilstošu burtu un skaitu).
        # alphabet - saraksts, kas izveidots ar latiņu alfabēta burtiem alfabētiska secība, kur katram burtam ir piekārtots skaitlis, kas parāda to burta biežumu.
        # alphabet tiek izveidots izmantojot SymbolCount.create_latin_alphabet()
        # alphabet = SymbolCount.create_latin_alphabet()
        # symbol - simbols, kurš ir uzrakstīts ar Unicode skaitļi. Izvelēsimies kādu simbolu skaitu atjaunosim.

        symbol = symbol.upper()
        kods = ord(symbol)
        if 65 <= kods <= 90:
            index = kods - 65
            alphabet[index].skaits += 1

    @staticmethod
    def update_symbol_count_for_all_text(alphabet, text):
        # Atjauno simbolu (burtu) skaitu visam tekstam mainīgajā alphabet.
        # text - simbolu virkne (str), kurai atjaunosim visu burtu biežumu vērtības.
        # alphabet - saraksts, kas izveidots ar latiņu alfabēta burtiem alfabētiska secība, kur katram burtam ir piekārtots skaitlis, kas parāda to burta biežumu.
        # alphabet tiek izveidots izmantojot SymbolCount.create_latin_alphabet()
        # alphabet = SymbolCount.create_latin_alphabet()

        for char in text:
            SymbolCount.update_symbol_count(alphabet, char)

    @staticmethod
    def print_symbols_by_frequency(alphabet):
        # Izvada lietotājam alphabeta visus burtus dilstoša secība pēc burtu biežuma. Izmanto print.
        # alphabet - saraksts, kas izveidots ar latiņu alfabēta burtiem alfabētiska secība, kur katram burtam ir piekārtots skaitlis, kas parāda to burta biežumu.
        # alphabet tiek izveidots izmantojot SymbolCount.create_latin_alphabet()
        # alphabet = SymbolCount.create_latin_alphabet()
        # Atgriež None
        # Izvada jau sakartotu alfabētu, piemēram šādi:
        # E 10
        # T 5
        # A 4
        # I 3
        # N 3
        # ... (utt)

        sorted_alphabet = SymbolCount.sort_sella_dilstosa(alphabet)
        for obj in sorted_alphabet:
            print(obj.burts, obj.skaits)

    @staticmethod
    def sort_sella_dilstosa(a):
        # Sakārto masīvu dilstošā secībā, izmantojot Šellas metodi (Shell sort)
        # a - saraksts (masīvs).
        # Atgriež sakartotu masīvu dilstošā secībā.

        n = len(a)
        solis = (3 ** math.floor(math.log(2 * n + 1, 3)) - 1) // 2
        while solis >= 1:
            for k in range(0, solis):
                for i in range(solis + k, n, solis):
                    if a[i - solis].skaits < a[i].skaits:
                        x = a[i]
                        j = i
                        while a[j - solis].skaits < x.skaits:
                            a[j] = a[j - solis]
                            j = j - solis
                            if j == k:
                                break
                        a[j] = x
            solis = (solis - 1) // 3

        return a


def save_text_from_data_by_rows_to_variable(datne):
    # Atgriež visu nolasītu tekstu no .txt datnes kā vienu str mainīgu.
    # datne - datnes fails (piemēram, .txt fails).
    # Piemēram:
    # datne = "C:\\Users\\User\\Desktop\\teksts.txt"

    a = ""
    with open(datne, mode="r", encoding="utf-8") as datne:
        for rinda in datne:
            a = a + rinda
    return a


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


datne = "C:\\Users\\User\\Desktop\\liels_teksts_eng.txt"  # datne - ceļš līdz failām. Jāraksta ceļu ar \\

text = save_text_from_data_by_rows_to_variable(datne)  # Nolasam tekstu no datnes kā str.

# Izveido sarakstu ar visiem latiņu alfabēta burtiem (īstenība ar visiem angļu valodas alfabēta burtiem),
# kur katram burtam izmantojot klasi SymbolCount tiek piekārtots "skaits".
# Ejam pa ciklu un "saraksts.append(SymbolCount(burts, skaits))".

# Izveido alfabēta sarakstu (caur klasi SymbolCount), kur katram burtam ir piekārtots reižu skaits, cik tas parādas tekstā.
# Tas mainīgais ir līdzīgs šadam sarakstam ar kortēžiem iekšā:
#  [("A", 0), ("B", 0), ("C", 0), ... , ("Z", 0)]
alphabet = SymbolCount.create_latin_alphabet()

SymbolCount.update_symbol_count_for_all_text(alphabet, text)  # Atjauno simbolu skaitu (burtu skaitu) katram simbolam (burtam) alfabēta.
SymbolCount.print_symbols_by_frequency(alphabet)  # Izvada visus simbolus (burtus) dilstoša skaita pēc biežuma.
