# Programmas nosaukums: Rekursija. Riņķa līnijas sešos virzienos.
# 5. uzdevums (1MPR02_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas izveido zemāk redzamo attēlu, izmantojot rekursiju.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


import tkinter
import math


logs = tkinter.Tk()
canva = tkinter.Canvas(logs, bg="white", height=1000, width=1000)
canva.pack()


def circles_six_directions(x, r, y):
    # Uzzīme riņķa līnijas sešos virzienos
    # x - x koordināta riņķa līnijas centram
    # r - r riņķa līnijas rādiuss
    # y - y koordināta riņķa līnijas centram
    if r <= 2:
        return
    canva.create_oval(x - r, y - r, x + r, y + r, width=3)

    circles_six_directions(x + 2 * r, r / 3, y)
    circles_six_directions(x - 2 * r, r / 3, y)

    circles_six_directions(x + r, r / 3, y - r * math.sqrt(3))
    circles_six_directions(x - r, r / 3, y - r * math.sqrt(3))

    circles_six_directions(x + r, r / 3, y + r * math.sqrt(3))
    circles_six_directions(x - r, r / 3, y + r * math.sqrt(3))


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


circles_six_directions(500, 100, 500)

logs.mainloop()
