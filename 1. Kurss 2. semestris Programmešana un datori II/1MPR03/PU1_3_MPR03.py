# Programmas nosaukums: Rekursija. V-koks.
# PU1.3 uzdevums (1MPR03_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas izveido zemāk redzamo attēlu, izmantojot rekursiju.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


import math
import tkinter


def zimet(x, y, garums):
    # uzzīmē rekursīvi "koku"
    # x - pirmā nogriežņa x koordināta
    # y - pirmā nogriežņa y koordināta
    # garums - pirmā nogriežņa garums (pēc tā tiek izrēķinātas koordinātas nepieciešamas, lai uzzīmēt nogriezni)
    lx = x + garums * math.cos(math.pi * 7 / 4) # -1*math.pi / 4 (-45 gradi)
    ly = y + garums * math.sin(math.pi * 7 / 4) # -1*math.pi / 4 (-45 gradi)

    lenkis = -1 * math.pi / 2 + math.pi * 7 / 4
    rx = x + garums * math.cos(lenkis)
    ry = y + garums * math.sin(lenkis)

    kanva.create_line(x, y, lx, ly)
    kanva.create_line(x, y, rx, ry)

    if garums > 1: # Stop kad garums nogrieznim ir mazāks nekā 1
        zimet(lx, ly, garums / 2)
        zimet(rx, ry, garums / 2)


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


logs = tkinter.Tk()
kanva = tkinter.Canvas(logs, width=1000, height=1000)
kanva.pack()

zimet(500, 800, 350)

logs.mainloop()
