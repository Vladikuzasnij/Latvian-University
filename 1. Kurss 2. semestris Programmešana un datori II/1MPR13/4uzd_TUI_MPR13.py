# Programmas nosaukums: Veikals
# 4.uzdevums (1MPR13_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas realizē iepirkšanos veikalā. Tiek nodrošināta iegādāto preču ievade (nosaukums, daudzums un cena)
# un "pirkumu čeka" izdrukāšana. (Vienkārša tekstuāla saskarne - 1 punkts, komplicēta grafiskā saskarne - 3 punkti.)
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


"""
UZDEVUMS TIKA REALIZĒTS AR TEKSTUALU SASKARNI.
"""


from random import randint


class Veikals:
    # Klase veikals.
    def __init__(self):
        # Izveidojam preces un selected_preces (izvelētas preces) vārdnīcas.
        # self.preces - vārdnica ar visam precem veikalā.
        # self.selected_preces - vārdnica ar lietotāja izvelētam precem.

        self.preces = dict()
        self.selected_preces = dict()

    def pievienot_preces(self, prece, cena, daudzums):
        # Metode veikala īpašniekam.
        # Preces pievienošana veikalām. Atjaunojam vārdnicu self.preces, preci, ar norādītu cenu un daudzumu.
        # prece - preces nosaukums (str).
        # cena - preces cena par vienu vienumu (float).
        # daudzums - cik daudz preci jāpiegāda veikalām (naturāls skaitlis lielāks par 0) (int).

        self.preces[prece] = {"cena": cena, "daudzums": daudzums}

    def dzest_preces(self, prece):
        # Metode veikala īpašniekam.
        # Nodzēs norādītu preci no veikalā, nodzēs noradītu preci no saraksta.
        # prece - preces nosaukums (str).

        print(f"Prece \"{prece}\" tika izmesta Getliņu izgāztuvē.")
        del self.preces[prece]

    def paradit_izveletas_preces(self):
        # Izdruka visas lietotaja izvelētas preces.

        print("Jūsu izvelētas preces:")
        for prece, info in self.selected_preces.items():
            cena = info["cena"]
            daudzums = info["daudzums"]
            print(f"{prece} - cena: {cena:.2f}€ , daudzums: {daudzums}")

    def paradit_preces(self):
        # Izdruka visas veikalā pieejamas preces lietotājam.

        print("Pieejamas preces veikalā:")
        for prece, info in self.preces.items():
            cena = info["cena"]
            daudzums = info["daudzums"]
            print(f"{prece} - cena: {cena:.2f}€ , daudzums: {daudzums}")

    def izveleties_preces(self, prece, daudzums):
        # Metode preces izvelēšanai lietotājam, jāizvēlas preci un to daudzumu.
        # prece - preces nosaukums (str).
        # daudzums - preces daudzums (int).

        if prece in self.preces:  # Ja tāda prece ir pieejama veikalā, tad tālak pārbaudam.
            if daudzums > self.preces[prece]["daudzums"]:  # Ja pieprasītais daudzums ir lielāks nekā ir veikalā, tad paziņojam, ka nevar nopirkt.
                print(f"Kļūda! Veikalā nav tik daudz preču! Precei \"{prece}\" pieejamais daudzums: {self.preces[prece]['daudzums']}")
            else:
                self.preces[prece]["daudzums"] -= daudzums  # Atņēmam nopirktu daudzumu.
                if prece not in self.selected_preces:
                    self.selected_preces[prece] = {"cena": self.preces[prece]["cena"], "daudzums": daudzums}
                else:
                    self.selected_preces[prece]["daudzums"] += daudzums  # Pievienojam daudzumu, cik daudz preces izvelējamies nopirkt.
                print(f"Izvēlētas preces: {prece}, cena: " + str(format(self.preces[prece]["cena"], ".2f")) + f"€ , daudzums: {daudzums}")
        else:
            print(f"Kļūda! Prece \"{prece}\" nav pieejama veikalā!")  # Ja tādas preces nav veikalā, tad paziņojam to.

    def atteikt_prece(self, prece, daudzums=None):
        # Lietotājs var atgriezt veikālā kādu no jau izvelētam precem ar norādīto daudzumu.
        # Ja lietotājs nenorāda daudzumu, tad tiek atgriezti visas preces.
        # prece - preces nosaukums (str).
        # daudzums - preces daudzums (int).

        if prece in self.selected_preces:
            if daudzums is None:  # Ja lietotājs nenorāda daudzumu, tad tiek atgriezti visas preces.
                daudzums = self.selected_preces[prece]["daudzums"]

            if daudzums > self.selected_preces[prece]["daudzums"]:  # Ja lietotājs grib atgriezt vairāk nekā paņem, tad kļūda.
                print(f"Kļūda! Precei \"{prece}\" ir izvēlēts mazāks daudzums. Nevar atgriezt vairāk nekā paņemat!")
            elif daudzums < 0:  # Ja lietotājs grib atgriezt negatīvu daudzumu, tad kļūda.
                print(f"Kļūda! Nevar atgriezt negatīvu daudzumu!")
            elif daudzums == 0:  # Ja lietotājs grib atgriezt neko, tad kļūda.
                print(f"Kļūda! Nevar atgriezt neko!")
            else:
                self.selected_preces[prece]["daudzums"] -= daudzums  # Atņēmam noradītu daudzumu no izvelētam precēm.
                self.preces[prece]["daudzums"] += daudzums  # Pievienojam noradītu daudzumu par izvelētam precēm.
                if self.selected_preces[prece]["daudzums"] == 0:  # Ja atņēmam tik daudz, ka vairāk tadas preces nav (nav izvelēta), tad nodzēsam to.
                    del self.selected_preces[prece]
                print(f"Izvēlētā prece \"{prece}\" tika atgriezta veikalā. Atgrieztais daudzums: {daudzums}")  # Paziņojam lietotājam informāciju.
        else:
            print(f"Kļūda! Prece netika \"{prece}\" izvēlēta.")  # Paziņojam lietotājam.

    def pirkumu_cekis(self):
        # Izdruka pirkumu lietotājam "pirkumu čeku", ar izvelētam precēm.
        total_price = 0

        print("---------------- ČEKS ----------------")
        print("SIA \"MAKSIMA\" Latvija")
        print("Veikals \"Maksima\"")
        print("Dārza iela 21, Bauska, t.22813371")
        print("Juridiskā adrese: \"Abras\", Krustkalni,")
        print("Ķekavas pagasts, Ķekavas novads, LV-2222")
        print("Čeks " + str(randint(100, 999)) + "/" + str(randint(100, 999)) + "                   #" + str(randint(10000000, 99999999)))
        print("==========================================")

        for prece, info in self.selected_preces.items():
            cena = info["cena"]
            daudzums = info["daudzums"]
            preces_cena = cena * daudzums
            total_price += preces_cena
            print(f"{prece} - cena: {cena:.2f}€, daudzums: {daudzums}, {preces_cena:.2f}€")

        print("==========================================")
        print(f"Kopā apmaksai: {total_price:.2f}€")
        print(f"Nopelnīta \"MAKSIMA\" nauda: {total_price * 0.01:.2f}€")
        print("---------------------------------------")


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


veikals = Veikals()

veikals.pievienot_preces("Āboli", 1.00, 50)
veikals.pievienot_preces("Piens", 1.40, 20)
veikals.pievienot_preces("Olas", 1.50, 30)
veikals.pievienot_preces("Pipari", 1.00, 100)

veikals.paradit_preces()
print()

veikals.dzest_preces("Piens")
print()

veikals.paradit_preces()
print()

veikals.izveleties_preces("Olas", 60)
veikals.izveleties_preces("Olas", 30)
veikals.izveleties_preces("Vārdnīca", 1)
veikals.izveleties_preces("Āboli", 50)
veikals.izveleties_preces("Pipari", 66)
print()

veikals.paradit_izveletas_preces()
print()

veikals.atteikt_prece("Āboli", 30)
veikals.atteikt_prece("Olas")
print()

veikals.paradit_izveletas_preces()
print()

veikals.atteikt_prece("Āboli", -10)
print()

veikals.paradit_izveletas_preces()
print()

veikals.atteikt_prece("Āboli", 0)
veikals.paradit_izveletas_preces()
print()
print()

veikals.pirkumu_cekis()
print()
print()

veikals.paradit_preces()
