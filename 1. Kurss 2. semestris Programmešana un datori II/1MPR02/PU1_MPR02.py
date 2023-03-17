# Programmas nosaukums: Rekursija. Krusti četros virzienos.
# Papilduzdevums 1. (1MPR02_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas izveido zemāk redzamo attēlu, izmantojot rekursiju.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


import tkinter
import math


logs = tkinter.Tk()
canvas = tkinter.Canvas(logs, bg="white", height=1000, width=1000)
canvas.pack()


def draw_line(x0, y0, x1, y1):
    # Uzzīme nogriežņi pēc diviem dotiem punktiem ar biezumu (width) 2
    # x0 - x koordināta sākumpunktam
    # y0 - y koordināta sākumpunktam
    # x1 - x koordināta galapunktam
    # y1 - y koordināta galapunktam
    canvas.create_line(x0, y0, x1, y1, width=2)


def draw_crosses(x0, y0, x1, y1, rekursijas_skaits):
    # Rekursīvi uzzīme krustiņus. Koeficienti tika iegūti aptuveni.
    # x0 - x koordināta sākumpunktam (nogriežņim)
    # y0 - y koordināta sākumpunktam (nogriežņim)
    # x1 - x koordināta galapunktam (nogriežņim)
    # y1 - y koordināta galapunktam (nogriežņim)
    length = math.sqrt((x1 - x0)**2 + (y1 - y0)**2)

    if rekursijas_skaits == 0:
        return

    angle = math.atan2(y1 - y0, x1 - x0) # math.atan2() atgriež y/x arktangensu radiānos. Kur x un y ir punkta (x,y) koordinātas.

    draw_line(x0, y0, x1, y1)

    dx = math.cos(angle + math.pi / 4) * length / 2.3 # izmaiņa pēc x
    dy = math.sin(angle + math.pi / 4) * length / 2.3 # izmaiņa pēc y
    draw_crosses(x1, y1, x1 + dx, y1 + dy, rekursijas_skaits - 1)

    dx = math.cos(angle - math.pi / 4) * length / 2.3
    dy = math.sin(angle - math.pi / 4) * length / 2.3
    draw_crosses(x1, y1, x1 + dx, y1 + dy, rekursijas_skaits - 1)

    dx = math.cos(angle + math.pi * 3 / 4) * length / 2.3
    dy = math.sin(angle + math.pi * 3 / 4) * length / 2.3
    draw_crosses(x1, y1, x1 + dx, y1 + dy, rekursijas_skaits - 1)

    dx = math.cos(angle - math.pi * 3 / 4) * length / 2.3
    dy = math.sin(angle - math.pi * 3 / 4) * length / 2.3
    draw_crosses(x1, y1, x1 + dx, y1 + dy, rekursijas_skaits - 1)


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


draw_crosses(500, 900, 500, 400, 5)

logs.mainloop()
