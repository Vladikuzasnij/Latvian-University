# Programmas nosaukums: Rekursija četri Serpinska trijstūri.
# PU1.2 uzdevums (1MPR03_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas izveido zemāk redzamo attēlu, izmantojot rekursiju.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


import tkinter


def draw_serpinskis(x1, y1, x2, y2, x3, y3, rekursijas_skaits):
    # uzzimē vienu Serpinska trijsturi izmantojot rekursiju
    # x1 - vislielāka trijstūra koordināta x vienai virsotnei
    # y1 - vislielāka trijstūra koordināta y vienai virsotnei
    # x2 - vislielāka trijstūra koordināta x otrai virsotnei
    # y2 - vislielāka trijstūra koordināta y otrai virsotnei
    # x3 - vislielāka trijstūra koordināta x trešai virsotnei
    # y3 - vislielāka trijstūra koordināta y trešai virsotnei
    # rekursijas_skaits - rekursijas skaits (cik līmeņus ir jāuzzīme Serpinska trijstūri)

    if rekursijas_skaits == 0:
        kanva.create_polygon(x1, y1, x2, y2, x3, y3, fill='white', outline='black')
    else:
        x1x2 = (x1 + x2) / 2
        y1y2 = (y1 + y2) / 2
        x1x3 = (x1 + x3) / 2
        y1y3 = (y1 + y3) / 2
        x2x3 = (x2 + x3) / 2
        y2y3 = (y2 + y3) / 2

        draw_serpinskis(x1, y1, x1x2, y1y2, x1x3, y1y3, rekursijas_skaits - 1)
        draw_serpinskis(x2, y2, x1x2, y1y2, x2x3, y2y3, rekursijas_skaits - 1)
        draw_serpinskis(x3, y3, x1x3, y1y3, x2x3, y2y3, rekursijas_skaits - 1)


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


logs = tkinter.Tk()

kanva = tkinter.Canvas(logs, width=1200, height=1300, bg='white')
kanva.pack()

x1 = 400
y1 = 350

x2 = 780
y2 = 350

x3 = 1180
y3 = 10

rekursijas_skaits = 5

draw_serpinskis(x1, y1, x2, y2, x3 / 2, y3, rekursijas_skaits)
draw_serpinskis(x1, y1, x2 - x1 + 20, y1 + y2, x3 - 1100, y3 + 500, rekursijas_skaits)
draw_serpinskis(x1 + 380, y1 + 350, x2 - x1 + 20, y1 + y2, x3 - 595, y3 + 1000, rekursijas_skaits)
draw_serpinskis(x1 + 380, y1, x2 - x1 + 400, y1 + y2, x3 - 100, y3 + 500, rekursijas_skaits)

logs.mainloop()
