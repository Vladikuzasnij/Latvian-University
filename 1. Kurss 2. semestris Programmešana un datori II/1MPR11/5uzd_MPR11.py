# Programmas nosaukums: "Biļešu paradīze" ar klasēm.
# 5. uzdevums (1MPR11_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas realizē teātra biļešu iegādi līdzīgi kā "Biļešu paradīze" izmantojot grafisko saskarni un OOP pieeju uzdevuma atrisināšanai.
# Uz ekrāna ir redzama skatītāju zāle ar visām sēdvietām un ar peles klikšķi var izvēlēties vienu vai vairākas biļetes,
# vai arī atcelt iepriekšējo izvēli. Pēc pogas Pirkt piespiešanas izvēlētas sēdvietas kļūst nepieejamas.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0

import tkinter
import random


class Seat:
    # Sēdvietu klase.
    def __init__(self, theater, rinda, kolonna):
        # Sēdvietu iniciālizēšana.
        self.status = 0  # Pirmkārt iestāsim, ka visas sēdvietas ir brīvas.
        if random.randint(0, 1) == 1:  # Nejaušam sēdvietu izvietojumam. Nevienmēr būs 50%. Jo random ir katrai sēdvietai, vai nu 0 vai 1 un tāpēc nebūs precīzi 50% katru reizi. Atkarīgs no veiksmes (liekas, ka tas ir labāk, jo interesantāk).
            self.status = 1  # Ja tiek izlozēts 1 (50% varbūtība), tad vieta ir aizņemta.
            self.button = tkinter.Button(theater, bg="#A00000", text="╳", width=5, height=2)  # Izkrāsojam vietu ar sarkanu krāsu un liksim ╳ simbolu.
        else:  # Ja netika izlozēts 1 (tad izlozēts 0), tad vieta nebūs aizņemta.
            self.button = tkinter.Button(theater, bg="green", text="○", width=5, height=2, command=self.change_status)  # Izkrāsojam vietu ar zaļu krāsu un liksim ○ simbolu.
        self.button.grid(row=rinda, column=kolonna)  # Definēsim, kur likt pogu.

    def change_status(self):
        # Izmaina pogas stātusu no 0 -> 2, no 2 -> 0, no 1 -> 1.
        # 0 - brīva vieta.
        # 1 - aizņemta vieta.
        # 2 - izvēlēta vieta.

        if self.status == 0:  # 0 -> 2 (brīva vieta uz izvelētu vietu)
            self.status = 2
            self.button.config(bg="yellow")  # dzeltens reprezentē izvēlētu vietu.
        elif self.status == 2:  # 2 -> 0 (izvelēta uz brīvu, atcelt)
            self.status = 0
            self.button.config(bg="green", text="○")  # zaļš reprezentē brīvo vieta.
        elif self.status == 1:  # Aizņemts. To nevar izmainīt. 1 -> 1.
            pass

    def occupy(self):
        # Komanda sēdvietas aizņemšanai.

        self.status = 1  # Pogas (vietas) statuss ir 1 (aizņemts).
        self.button.configure(bg="#A00000", text="╳")  # Izmainām krāsu uz sarkanu un izmainām tekstu uz pogas uz "╳".


class Teatris:
    # Teātra klase.
    def __init__(self, theater, rindas, kolonnas):
        self.seats = []
        self.selected_seats = []  # Izvelētas sēdvietas saraksts.
        self.num_occupied_seats = 0  # Nepieciešams, lai sekot līdzi aizņemto sēdvietu skaitam.

        for i in range(rindas):  # Izmantojot pilno pārlasi pārbaudam, vai visas vietas nav aizņemtas (varbūt ka "paveicas" un uzreiz viss ir izpārdots).
            rinda = []
            for j in range(kolonnas):
                seat = Seat(theater, i, j)
                if seat.status == 1:
                    self.num_occupied_seats += 1  # Ja sēdvieta sākotnēji ir aizņemta, tad palieliniet skaitītāju.
                rinda.append(seat)
            self.seats.append(rinda)
        self.buy_button = tkinter.Button(theater, text="Nopirkt izvēlētās biļetes", command=self.buy_tickets)  # Nopirkšanas poga.
        self.buy_button.grid(row=rindas + 1, column=0, columnspan=kolonnas)
        self.all_seat_quantity = len(self.seats) * len(self.seats[0])  # Lai zinātu cik ir kopējais sēdvietu skaits.
        self.check_occupied()  # Izsaucam check_occupied, lai atjauninātu nopirkšanas pogas stāvokli (ja visas ir aizņemtas vietas, tad bloķēt pogu).

    def read_selection(self):
        # Atgriež sarakstu ar izvēlētam sēdvietam izmantojot pilnu pārlasi caur kātru vietu (rindu un kolonnu).
        selected_seats = []  # Tukšais saraksts ar izvēlētam sēdvietam.
        for row in self.seats:  # Iterējam caur katru rindu un kolonnu (pilnā pārlase)
            for seat in row:
                if seat.status == 2:  # Un izmantojot pilno pārlasi, ja sēdvietai ir piekārtots 2 (izvelēta), tad .append sēdvietu sarakstam selected_seats (izvēlētas sēdvietas)
                    selected_seats.append(seat)  # Pievienojam sarakstam atrasto izvēlēto vietu.
        return selected_seats  # Atgriezt izvēlētas sēdvietas.

    def buy_tickets(self):
        # Komanda pirkšanas pogai. Izsauc seat.occupy() visiem sēdvietam kas ie izvēlētas un palielina num_occupied_seats par katru izvēlēto vietu (tas ir nepieciešāms, lai jā visas vietās ir aizņemtas, tad bloķēt pogu).
        self.selected_seats = self.read_selection()  # Saraksts ar visam izvēlētam sēdvietam.
        for seat in self.selected_seats:  # Izmainām vērtības visam izvēlētam vietam (izmainām 2 -> 1) un palielinām self.num_occupied_seats par vienu.
            seat.occupy()  # Izmainīt sēdvietas stavokļi uz ieņemtu.
            self.num_occupied_seats += 1  # Palielinam aizņemto vietu skaitītāju par katru tikko aizņemto vietu.
        self.check_occupied()  # Izsaukt check_occupied, lai atjauninātu etiķetes un pogas stāvokli.

    def check_occupied(self):
        # Komanda pārbauda vai visas vietas jau ir izpārdotas. Ja ir, tad bloķē pirkšanas pogu.
        if self.num_occupied_seats == self.all_seat_quantity:  # Ja visas vietas ir aizņemtas, tad nobloķēt pirkšanas pogu. Salidzina aizņemto vietu skaititāju, ar visu sēdvietu skaitu. Ja sakrīt tad, bloķēt pogu.
            self.buy_button.config(text="Visas vietas izpārdotas!", state="disabled")  # Bloķēt pirkšanas pogu un izmainīt tekstu uz pogas.


class Define_Theater:
    # Klase teātra definēšanai.
    @staticmethod
    def izveidot_teatri():
        # Metode, kas nolasa ievādītas rindas un kolonnu vērtības no entry, nodzēs palīglogu teātra definēšanai, un izveido "zale" windows un izsauc klasi Teatris.
        rindas = int(rindas_entry.get())  # Nolasam vērtības no rindas entry.
        kolonnas = int(kolonnas_entry.get())  # Nolasam vērtības no kolonnas (sēdvietas) entry.

        logs.destroy()  # Nodzēsam logu, kur mēs prāsījam lietotājam ievādīt rindas un sēdvietu skaitu.

        zale = tkinter.Tk()  # Izveidojam jauno logu teātrim.
        zale.title("Zāle")  # Jauna loga virsraksts.
        Teatris(zale, rindas, kolonnas)  # Izsauc Teātra klasi ar lietotāja ievādītam rindam un kolonnam.
        zale.mainloop()  # Lai jauns logs būtu redzāms.


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


# Izveidojam logu, kur paprasām lietotājam ievādīt rindas un kolonnu (sēdvietu) skaitu teātrī. Tas ir nepieciešams teātra izveidošanai.
logs = tkinter.Tk()  # Faktiski tas ir papildlogs, lai lietotājs varētu ievādit rindas un kolonnu skaitu teātrī.
logs.title("Biļešu paradīze")  # Loga virsraksts.
logs.geometry("250x125")  # Loga izmērs.

rindas_label = tkinter.Label(logs, text="Rindu skaits:")  # Etiķete, lai lietotājs zinātu, ka jāievāda rindu skaitu.
rindas_label.pack()

rindas_entry = tkinter.Entry(logs)  # Entry (ievaddlaukums) lietotājam rindas ievadei.
rindas_entry.pack()

kolonas_label = tkinter.Label(logs, text="Sēdvietu skaits:")  # Etiķete, lai lietotājs zinātu, ka jāievāda sēdvietu (kolonnu) skaitu.
kolonas_label.pack()

kolonnas_entry = tkinter.Entry(logs)  # Entry (ievaddlaukums) lietotājam sēdvietu (kolonnas) ievadei.
kolonnas_entry.pack()

poga_izveidot = tkinter.Button(logs, text="Izveidot teātru", command=Define_Theater.izveidot_teatri)  # Poga "Izveidot teātru" papildlogam. Izsauc komandi "Define_Theater.izveidot_teatri"
poga_izveidot.pack()

logs.mainloop()  # Lai logs būtu redzāms.
