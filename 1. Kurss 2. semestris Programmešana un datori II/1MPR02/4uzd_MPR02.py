# Programmas nosaukums: Rekursija. Riņķa līnijas četri virzieni.
# 4. uzdevums (1MPR02_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas izveido zemāk redzamo attēlu, izmantojot rekursiju.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


import tkinter


logs = tkinter.Tk()
canva = tkinter.Canvas(logs, bg="white", height=600, width=600)
canva.pack()


def circles_four_directions(x, r, y):
    # Uzzīme riņķa līnijas četros virzienos
    # x - x koordināta riņķa līnijas centram
    # r - r riņķa līnijas rādiuss
    # y - y koordināta riņķa līnijas centram
    if r <= 3:
        return
    canva.create_oval(x - r, y - r, x + r, y + r, width=2)
    circles_four_directions(x + r, r // 2, y)
    circles_four_directions(x - r, r // 2, y)
    circles_four_directions(x, r // 2, y - r)
    circles_four_directions(x, r // 2, y + r)


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


circles_four_directions(300, 100, 300)

logs.mainloop()
