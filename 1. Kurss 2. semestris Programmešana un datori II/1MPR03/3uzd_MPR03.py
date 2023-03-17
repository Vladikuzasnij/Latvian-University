# Programmas nosaukums: Koha zvaigzne
# 3. uzdevums (1MPR03_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas izveido Koha zvaigzni, izmantojot rekursiju.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


import math
import tkinter


def zimet_koha_zvaigzni(x1, y1, x5, y5):
    # Rekursīvi uzzīme daļu no Koha zvaigznes
    # x1 - nogriežņa sākumpunkta x koordināta
    # y1 - nogriežņa sākumpunkta y koordināta
    # x5 - nogriežņa galapunkta x koordināta
    # y5 - nogriežņa galapunkta y koordināta
    if math.sqrt((x1 - x5)**2 + (y1 - y5)**2) < 4: # kad nogriežņa garums paliek mazāks par 4, tad pārtraucam rekursiju
        kanva.create_line(x1, y1, x5, y5)
    else:
        dx = x5 - x1
        dy = y5 - y1
        x2 = x1 + dx // 3
        y2 = y1 + dy // 3
        x3 = (x1 + x5) // 2 + math.sqrt(3) * (y1 - y5) // 6
        y3 = (y1 + y5) // 2 + math.sqrt(3) * (x5 - x1) // 6
        x4 = x1 + 2 * dx // 3
        y4 = y1 + 2 * dy // 3
        zimet_koha_zvaigzni(x1, y1, x2, y2)
        zimet_koha_zvaigzni(x2, y2, x3, y3)
        zimet_koha_zvaigzni(x3, y3, x4, y4)
        zimet_koha_zvaigzni(x4, y4, x5, y5)


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


logs = tkinter.Tk()
kanva = tkinter.Canvas(logs, bg="white", height=1000, width=1000)
kanva.pack()

zimet_koha_zvaigzni(250, 562, 792, 562)
zimet_koha_zvaigzni(792, 562, 521, 21)
zimet_koha_zvaigzni(521, 21, 250, 562)

logs.mainloop()
