# Programmas nosaukums: Latviešu alfabētu burtu biežums tekstā
# PU1. uzdevums (1MPR15_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas skaita, cik un kādi latviešu alfabēta burti (lielie un mazie burti netiek šķirti) satur dotais teksts.
# Rezultātu uz ekrāna izvada burtu biežuma dilstošā secībā.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


import math


class SymbolCountLv:
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
        # ("A", 972)

        return f'("{self.burts}", {self.skaits})'

    @staticmethod
    def create_latvian_alphabet():
        # Atgriež sarakstu ar lieliem latviešu alfabētu burtiem alfabētiska secība, kur katram burtam ir piekārtots skaits 0.
        # Lidzīgi kā atgriež tādu sarakstu ar kortežiem:
        # [("A", 0), ("Ā", 0), ("B", 0), ("C", 0), ("Č", 0), ("D", 0), ("E", 0), ("Ē", 0), ("F", 0), ("G", 0), ("Ģ", 0), ("H", 0), ("I", 0), ("Ī", 0), ("J", 0), ("K", 0), ("L", 0), ("Ļ", 0), ("M", 0), ("N", 0), ("Ņ", 0), ("O", 0), ("P", 0), ("R", 0), ("S", 0), ("Š", 0), ("T", 0), ("U", 0), ("V", 0), ("Z", 0), ("Ž", 0)]
        # Izmanto chr funkciju.

        mas = []
        lv = ["A", "Ā", "B", "C", "Č", "D", "E", "Ē", "F", "G", "Ģ", "H", "I", "Ī", "J", "K", "Ķ", "L", "Ļ", "M", "N", "Ņ", "O", "P", "R", "S", "Š", "T", "U", "Ū", "V", "Z", "Ž"]

        for i in range(len(lv)):
            burts = lv[i]
            skaits = 0
            mas.append(SymbolCountLv(burts, skaits))

        return mas

    @staticmethod
    def update_symbol_count(alphabet, x):
        # Atjauno (palielinā par vienu) simbolu (burtu) skaitu alphabet mainīgajā, konkrētāja vietā (kur ir tās noteikts kortežs ar atbilstošu burtu un skaitu).
        # alphabet - saraksts, kas izveidots ar latiņu alfabēta burtiem alfabētiska secība, kur katram burtam ir piekārtots skaitlis, kas parāda to burta biežumu.
        # alphabet tiek izveidots izmantojot SymbolCountLv.create_latvian_alphabet()
        # alphabet = SymbolCountLv.create_latvian_alphabet()
        # symbol - simbols, kurš ir uzrakstīts ar Unicode skaitļi. Izvelēsimies kādu simbolu skaitu atjaunosim.

        lv = ["A", "Ā", "B", "C", "Č", "D", "E", "Ē", "F", "G", "Ģ", "H", "I", "Ī", "J", "K", "Ķ", "L", "Ļ", "M", "N", "Ņ", "O", "P", "R", "S", "Š", "T", "U", "Ū", "V", "Z", "Ž"]

        x = x.upper()
        if x in lv:
            index = lv.index(x)
            alphabet[index].skaits += 1

    @staticmethod
    def update_symbol_count_for_all_text(alphabet, text):
        # Atjauno simbolu (burtu) skaitu visam tekstam mainīgajā alphabet.
        # text - simbolu virkne (str), kurai atjaunosim visu burtu biežumu vērtības.
        # alphabet - saraksts, kas izveidots ar latiņu alfabēta burtiem alfabētiska secība, kur katram burtam ir piekārtots skaitlis, kas parāda to burta biežumu.
        # alphabet tiek izveidots izmantojot SymbolCount.create_latin_alphabet()
        # alphabet = SymbolCount.create_latin_alphabet()

        for char in text:
            SymbolCountLv.update_symbol_count(alphabet, char)

    @staticmethod
    def print_symbols_by_frequency(alphabet):
        # Izvada lietotājam alphabeta visus burtus dilstoša secība pēc burtu biežuma. Izmanto print.
        # alphabet - saraksts, kas izveidots ar latviešu alfabēta burtiem alfabētiska secība, kur katram burtam ir piekārtots skaitlis, kas parāda to burta biežumu.
        # alphabet tiek izveidots izmantojot SymbolCountLv.create_latvian_alphabet()
        # alphabet = SymbolCountLv.create_latvian_alphabet()
        # Atgriež None
        # Izvada jau sakartotu alfabētu, piemēram šādi:
        # L 2
        # Ļ 2
        # B 1
        # A 1
        # I 0
        # ... (utt)

        sorted_alphabet = SymbolCountLv.sort_sella_dilstosa(alphabet)
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
    # Uzrakstā termināla lietotājam visu tekstu no .txt failā pa rindam.
    # datne - datnes fails (piemēram, .txt fails)
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


datne = "C:\\Users\\User\\Desktop\\liels_teksts_lv.txt"  # datne - ceļš līdz failām.

text = save_text_from_data_by_rows_to_variable(datne)  # Nolasam tekstu no datnes kā str.

# Izveido sarakstu ar visiem latviešu alfabēta burtiem, kur katram burtam, izmantojot klasi SymbolCountLv, tiek piekārtots "skaits".
# Ejam pa ciklu un "saraksts.append(SymbolCountLv(burts, skaits))".

# Izveido alfabēta sarakstu (caur klasi SymbolCountLv), kur katram burtam ir piekārtots reižu skaits, cik tas parādas tekstā.
# Tas mainīgais ir līdzīgs šadam sarakstam ar kortēžiem iekšā:
#  [("A", 0), ("Ā", 0), ("B", 0), ("C", 0), ("Č", 0), ("D", 0), ... , ("Z", 0), ("Ž", 0)]
alphabet = SymbolCountLv.create_latvian_alphabet()

SymbolCountLv.update_symbol_count_for_all_text(alphabet, text)  # Atjauno simbolu skaitu (burtu skaitu) katram simbolam (burtam) alfabētā.
SymbolCountLv.print_symbols_by_frequency(alphabet)  # Izvada visus simbolus (burtus) dilstoša skaita pēc biežuma.
