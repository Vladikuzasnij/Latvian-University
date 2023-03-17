# Programmas nosaukums: Rekursija. Kvadrāti kvadrātos.
# PU1.4 uzdevums (1MPR03_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas izveido zemāk redzamo attēlu, izmantojot rekursiju.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


import math
import tkinter


def zimet_rekursivi(x0, y0, x2, y2, x1, y1, x3, y3):
    # Uzzīmē rekursīvi kvadrātus noteiktā secība
    # x0 - kreisā apakšēja stūra koordināta pēc x (runājot par 1. iterācijas kvadrātu)
    # y0 - kreisā apakšēja stūra koordināta pēc y (runājot par 1. iterācijas kvadrātu)

    # x2 - laba augšēja stūra koordināta pēc x (runājot par 1. iterācijas kvadrātu)
    # y2 - laba augšēja stūra koordināta pēc y (runājot par 1. iterācijas kvadrātu)

    # x1 - kreisā augšēja stūra koordināta pēc x (runājot par 1. iterācijas kvadrātu)
    # y1 - kreisā augšēja stūra koordināta pēc y (runājot par 1. iterācijas kvadrātu)

    # x3 - laba apakšēja stūra koordināta pēc x (runājot par 1. iterācijas kvadrātu)
    # y3 - laba apakšēja stūra koordināta pēc x (runājot par 1. iterācijas kvadrātu)

    # attālums no punkta (x0;y0) līdz (x1;y1)
    if math.sqrt((x0 - x1)**2 + (y0 - y1)**2) > 5: # ja attālums starp šiem punktiem paliek mazāks nekā 5 (kvadrāta mala paliek mazāka nekā 5), tad rekursija pārtraucās
        kanva.create_line(x0, y0, x2, y2)
        kanva.create_line(x2, y2, x1, y1)
        kanva.create_line(x1, y1, x3, y3)
        kanva.create_line(x3, y3, x0, y0)

        zimet_rekursivi((x0 + x2) / 2, (y0 + y2) / 2, (x2 + x1) / 2, (y1 + y2) / 2, (x1 + x3) / 2, (y1 + y3) / 2, (x3 + x0) / 2, (y0 + y3) / 2)


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


logs = tkinter.Tk()
kanva = tkinter.Canvas(logs, width=600, height=600)
kanva.pack()

x0 = 50
y0 = 50

x1 = 550
y1 = 550

x2 = x0
y2 = y1

x3 = x1
y3 = y0

zimet_rekursivi(x0, y0, x2, y2, x1, y1, x3, y3)

logs.mainloop()
