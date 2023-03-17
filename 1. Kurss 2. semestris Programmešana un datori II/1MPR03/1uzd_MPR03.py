# Programmas nosaukums: Serpinska trijstūris.
# 1. uzdevums (1MPR03_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas izveido zemāk redzamo attēlu, izmantojot rekursiju.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


import tkinter


def draw_serpinskis(x1, y1, x2, y2, x3, y3):
    # Uzzīmē Serpinskā trijstūri izmantojot rekursiju
    # x1 - x koordināta kreisai apakšējai trijstūra virsotnei
    # y1 - y koordināta kreisai apakšējai trijstūra virsotnei
    # x2 - x koordināta labai apakšējai trijstūra virsotnei
    # y2 - y koordināta labai apakšējai trijstūra virsotnei
    # x3 - x koordināta augšējai centrālai trijstūra virsotnei
    # y3 - y koordināta augšējai centrālai trijstūra virsotnei

    area = abs((0.5) * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))) # Trijstūra laukums

    if area < 10: # regulē rekursijas skaitu. Ja trijstūra laukums ir mazāks neka 10, tad stop
        kanva.create_polygon(x1, y1, x2, y2, x3, y3, fill='white', outline='black')
    else:
        x1x2 = (x1 + x2) / 2
        y1y2 = (y1 + y2) / 2
        x1x3 = (x1 + x3) / 2
        y1y3 = (y1 + y3) / 2
        x2x3 = (x2 + x3) / 2
        y2y3 = (y2 + y3) / 2

        draw_serpinskis(x1, y1, x1x2, y1y2, x1x3, y1y3)
        draw_serpinskis(x2, y2, x1x2, y1y2, x2x3, y2y3)
        draw_serpinskis(x3, y3, x1x3, y1y3, x2x3, y2y3)


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


logs = tkinter.Tk()

kanva = tkinter.Canvas(logs, width=1200, height=1200, bg='white')
kanva.pack()

x1 = 10
y1 = 1000
x2 = 1200
y2 = 1000
x3 = 1200
y3 = 10

draw_serpinskis(x1, y1, x2, y2, x3 / 2, y3)

logs.mainloop()
