# Programmas nosaukums: "Biļešu paradīze" ar GUI
# Papilduzdevums 1 (1MPR09_Vladislavs_Babaņins)
# Uzdevuma formulējums: Realizēt uzdevumu par biļešu iegādi tā, ka uz ekrāna ir redzamas visas sēdvietas un ar peles klikšķi (klikšķiem) var izvēlēties vienu (vairākas) biļetes.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


import tkinter
import numpy
import random

# global mainīgo saraksts:
# root, a, label2, buy_button


def result():
    # Komanda tiek izsaukta pēc "submit_button" nospiešanas ( = ).
    # Paņemt n un m no lietotāja un izveido matricu, kur aptuvēni 50% no matricas ir 1.
    # Izveido globālu mainīgu a un tas ir tās matrica.
    # Izsauc komandu show_array()

    global a
    n = input_rindas_skaits.get()
    m = input_kolonnas_skaits.get()
    n = int(n)
    m = int(m)
    arr = numpy.ones((n, m))
    num_ones = int(n * m * 0.5)
    ones_count = 0

    for i in range(n):
        for j in range(m):
            if ones_count < num_ones and random.random() < 0.5:
                arr[i][j] = 0
                ones_count = ones_count + 1
    a = arr
    show_array(a)


def toggle_button(poga):
    # Pogas sēdvietas izvelēšanai
    # 1 -> 1 "Vieta aizņemta!"
    # 0 -> X "Biļete izvelēta!"
    # X -> 0 "Biļete atcelta!"
    # check_button_text() pārbauda vai uz visām pogām ir uzrakstīts "1". (pilnā pārlase).
    # Ja uz visiem, tad blokēt pogas un uzrakstīt kā visas biļetes ir izpārdotas.

    if poga["text"] == "0":
        poga["text"] = "X"
        label2.config(text="Biļete izvelēta!")
        check_button_text()

    elif poga["text"] == "1":
        poga["text"] = "1"
        label2.config(text="Vieta aizņemta!")
        check_button_text()

    elif poga["text"] == "X":
        poga["text"] = "0"
        label2.config(text="Biļete atcelta!")
        check_button_text()


def change_button_text():
    # Pārlasa visas pogas root'ā un izmainā "X" uz "1" (izvelētus uz aizņemts)
    # Izmainām label2 tekstu uz "Nopirkts!"
    # Tiek izmantots globals mainīgais root

    global root

    for poga in root.grid_slaves():  # Parlasam visas pogas
        if type(poga) == tkinter.Button:
            if poga.cget("text") == "X":  # cget dot iespēju pārbaudit vai teksts uz pogas ir "X"
                poga.configure(text="1")

    label2.config(text="Nopirkts!")

    check_button_text()


def check_button_text():
    # Izmantojot divus karogus, pārbaudam vai uz visiem pogam ir uzrakstīts "1". (Pogas pilnā pārlase)
    # Ja uz visām ir "1", tad visas pogas bloķēt un uzrakstīt "Visas biļetes ir izpārdotas!"

    all_ones = True
    has_two = False  # two == X (jo pirmkārts tika izmantots 0 - brīvs, 1 - aizņemts, 2 - izvelēts)

    for poga in root.grid_slaves():  # Pilnā pārlase pogiem un label'iem kuri ir grid'ā izmantojot in root.grid_slaves() (atrādu internētā tādu funkciju)
        if poga.cget("text") == "1 - aizņemta vieta\n0 - brīva vieta\nX - izvelētas vietas pirkšanai\nIzvēlieties vietas pirkšanai!":
            continue
        if poga.cget("text") == "Nopirkt izvelētas biļetes":
            continue
        if poga.cget("text") == "Nopirkts!":
            continue
        if poga.cget("text") == "Biļete izvelēta!":
            continue
        if poga.cget("text") == "X":
            has_two = True
        if poga.cget("text") != "1":
            all_ones = False

    if all_ones:
        label3 = tkinter.Label(root, text="Visas biļetes ir izpārdotas!", font=("Arial", 12), anchor="ne")
        label3.place(relx=1.0, rely=0.0, anchor="ne")
        buy_button.config(state="disabled")

        for poga in root.grid_slaves():  # grid_slave() palīdz visas pogas bloķēt
            poga.config(state="disabled")

    elif not has_two:
        buy_button.config(state="disabled")

    else:
        buy_button.config(state="normal")


def button_callback(poga):
    # Definē callback() funkciju kas izsauc toggle_button(poga). Jā tieši tā neuzrakstīt, tad programma nestrādās
    def callback():
        toggle_button(poga)
    return callback


def show_array(a):
    # Izveido jaunu logu "root", un izveido tajā pogas (sēdvietas) nepieciešamā skaitā, ar komandu button_callback
    # Parada jaunu logu "root".
    # Tiek izveidota poga "Nopirkt izvelētas biļetes", pēc tas nospiešanas tiek izsaukta komanda change_button_text
    # Pogas ir dizaktivētas (disabled) pēc noklusējumā.
    # label2 ir izveidots tukšs un globāls, lai pēc tam to mainītu uz "Nopirkts!" vai uz "".
    # label4 ir izveidots informatīvam nolūkam
    # tiek izveidoti trīs globāli mainīgie
    global root, label2, buy_button

    root = tkinter.Tk()
    root.title("Teātris")

    rindas = len(a)
    kolonnas = len(a[0])
    pogas = []
    for i in range(rindas):
        for j in range(kolonnas):
            poga = tkinter.Button(root, text=str(int(a[i][j])), width=2, height=1)
            poga.config(command=button_callback(poga))
            poga.grid(row=i, column=j)
            pogas.append(poga)

    label2 = tkinter.Label(root, text="")
    label2.grid(row=i + 1, column=j + 1)

    label4 = tkinter.Label(root, text="1 - aizņemta vieta\n0 - brīva vieta\nX - izvelētas vietas pirkšanai\nIzvēlieties vietas pirkšanai!")
    label4.grid(row=i + 3, column=j + 3, sticky="s")

    buy_button = tkinter.Button(root, text="Nopirkt izvelētas biļetes", width=20, bd=1, command=change_button_text, state="disabled")
    buy_button.grid(row=i + 2, column=j + 2)

    check_button_text()

    root.mainloop()


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


logs = tkinter.Tk()  # Tkinter (lai izmantotu to komandas)
logs.geometry("170x130")  # Loga izmēra definēšana
logs.title("Biļešu nopirkšana")  # Windows "loga" nosaukums


# Labels teātrim
label_teatris = tkinter.Label(logs, text="Teātris", font=("Arial", 12))
label_teatris.place(x=20, y=6)

label_teatra_izmers = tkinter.Label(logs, text="Teātra izmērs:", font=("Arial", 12))
label_teatra_izmers.place(x=20, y=30)

label_x = tkinter.Label(logs, text="x", font=("Arial", 15))
label_x.place(x=56, y=58)


# Entry logi
input_rindas_skaits = tkinter.Entry(logs, width=3)
input_rindas_skaits.place(x=30, y=65)

input_kolonnas_skaits = tkinter.Entry(logs, width=3)
input_kolonnas_skaits.place(x=75, y=65)

# -----------------------------------------

submit_button = tkinter.Button(logs, text="=", width=20, bd=1, command=result)  # Izmantojam definētas komandas, lai pēc pogas nospiešanas tā komanda tiek izpildīta
submit_button.place(x=110, y=62, width=25)  # Parādam, kur poga tiks attēlota

logs.mainloop()  # lai logs būtu redzāms visu laiku
