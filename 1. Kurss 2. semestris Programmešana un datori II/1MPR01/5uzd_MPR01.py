# Programmas nosaukums: Kardīoda zīmējums
# 5. uzdevums (1MPR01_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas uzzīmē kardioīdu, kuras vienādojums parametriskā formā ir
# x=a(2cosφ-cos2φ)
# y=a(2sinφ-sin2φ)
# Kur φ∈[0;2π], bet parametru a ievada no tastatūras. Koordinātu sistēma jāizvēlas tā, lai attēls būtu pa visu ekrānu, neatkarīgi no a vērtības.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


import math
import tkinter
from tkinter import ttk
from tkinter import *


def enable_button_linija(): # Aktīve pogu "Parādīt funkciju"
    # Aktive pogu "Linija", kura parāda kardioīdu
    poga3['state'] = ACTIVE


def disable_button_linija(): # Dizaktīve pogu "Parādīt funkciju"
    # Padara pogu "Linija" par neaktīvu, kura parāda kardioīdu
    poga3['state'] = DISABLED


def enable_button_plakne(): # Dizaktīve pogu "Parādīt funkciju"
    # Padara pogu "Plakne" par aktīvu, kura parāda plakni
    poga1['state'] = ACTIVE


def disable_button_plakne(): # Dizaktīve pogu "Parādīt funkciju"
    # # Padara pogu "Plakne" par neaktīvu, kura parāda kardioīdu
    poga1['state'] = DISABLED


def notirit():
    # Kanvas satura dzēšanai un dizaktivē pogu "Līnija"
    kanva.delete("all")
    disable_button_linija()


def is_real_number_in_entry(event):
    # Parbauda vai e1 entry logā ir ierakstīts reāls skaitlis
    # Padara tā, ka poga "Plakne" ir aktīva tikai tad, ja entry logā ir ierakstīts reāls skaitlis
    # Padara tā, ka poga "Līnija" ir aktīva tikai tad, ja tika nospiests uz pogu "Plakne"
    # Tas ir izdārīts, lai nevarētu uzzīmēt līnju, bez uzzimētas plaknes
    # event - simbolu ierakstīšana entry logā
    disable_button_plakne()
    disable_button_linija()
    kanva.delete("all")
    try:
        float(e1.get()) # Pārbaude no e1 ņemsim simbolu virkni un pārbaudīsim vai to var pārveidot float
    except:
        disable_button_plakne()
        disable_button_linija()
        kanva.delete("all")

    else:
        if float(e1.get()) > 0:
            enable_button_plakne()
        else:
            disable_button_plakne()
            disable_button_linija()
            kanva.delete("all")


def paradit():
    # Koordinātu plaknes uzzīmēšana, kura pielāgojas atkarība no a (Lai tāda veidā parādīt kardioīda izmēru).
    enable_button_linija()
    a = float(e1.get())
    kanva.create_line(150, 350, 850, 350, fill="gray")
    kanva.create_line(845, 345, 850, 350, fill="gray")
    kanva.create_line(845, 355, 850, 350, fill="gray")
    kanva.create_text(845, 330, text="X", anchor="nw", font=("Helvetica", 10), fill="gray")
    kanva.create_line(500, 0, 500, 700, fill="gray")
    kanva.create_line(505, 5, 500, 0, fill="gray")
    kanva.create_line(495, 5, 500, 0, fill="gray")
    kanva.create_text(505, 0, text="Y", anchor="nw", font=("Helvetica", 10), fill="gray")

    for i in range(175, 826, 25):
        kanva.create_line(i, 347, i, 353, fill="gray")
    #kanva.create_text(175, 330, text = str(-3*a), anchor = "nw", font = ("Helvetica",10), fill = "gray")
    #kanva.create_text(591, 330, text = str(a), anchor = "nw", font=("Helvetica", 10), fill = "gray")

    for i in range(25, 676, 25):
        kanva.create_line(497, i, 503, i)
    #kanva.create_text(505, 603, text = str(-2.5*a), anchor = "nw", font = ("Helvetica", 10), fill = "gray")
    #kanva.create_text(505, 80, text = str(2.5*a), anchor = "nw", font = ("Helvetica", 10), fill = "gray")

    for i in range(-13, 0): # minusiem uz X
        kanva.create_text(490 + i * 25, 330, text=str(i * a / (4)), anchor="nw", fill="gray")

    for i in range(1, 14): # plusiem uz X
        kanva.create_text(496 + i * 25, 330, text=str(i * a / (4)), anchor="nw", fill="gray")

    for i in range(-13, 0): # minusiem uz Y
        kanva.create_text(505, 341 - i * 25, text=str(i * a / (4)), anchor="nw", fill="gray")

    for i in range(1, 14): # minusiem uz X
        kanva.create_text(505, 341 - i * 25, text=str(i * a / (4)), anchor="nw", fill="gray")


def polari():
    # Līnijas uzzīmēšana

    x0 = 500
    y0 = 350
    a = float(e1.get())

    lenght = a
    b = 4
    a = b

    b = 2 * x0 + a / 25
    x1 = x0 + a / 25
    y1 = y0

    # Līnija
    for i in range(1, 3600, 1):

        f = i / 1800 * math.pi
        x = a * (2 * math.cos(f) - math.cos(2 * f))

        y = a * (2 * math.sin(f) - math.sin(2 * f))
        y2 = -y * 25 + y0
        x2 = x * 25 + x0

        kanva.create_line(x1, y1, x2, y2)
        x1 = x2
        y1 = y2

# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


logs = tkinter.Tk()
logs.title("Kardīoda")
logs.geometry("1200x760")
kanva = tkinter.Canvas(logs, bg="white", height=750, width=1000)
kanva.place(x=160, y=0)
poga1 = ttk.Button(logs, text="Plakne", command=paradit, state='disabled')
poga1.place(x=10, y=10)
poga2 = ttk.Button(logs, text="Notīrīt", command=notirit)
poga2.place(x=10, y=50)
poga3 = ttk.Button(logs, text="Līnija", command=polari, state='disabled')
poga3.place(x=10, y=100)

# Entry
e1 = ttk.Entry(logs)
e1.bind("<KeyRelease>", is_real_number_in_entry) # Izsaucam funkciju is_real_number_in_entry
e1.place(x=33, y=150, width=30)

l0 = ttk.Label(logs, text="x = a(2cos(phi) - cos(2phi))")
l0.place(x=13, y=180)

l1 = ttk.Label(logs, text="y = a(2sin(phi) - sin(2phi))")
l1.place(x=13, y=200)

l2 = ttk.Label(logs, text="{", font=("Helvetica", 30))
l2.place(x=-2, y=174)

l3 = ttk.Label(logs, text="a = ")
l3.place(x=9, y=150)

disable_button_linija()

logs.mainloop()
