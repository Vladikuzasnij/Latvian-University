# Programmas nosaukums: Rekursija ar riņķa līnijām un kvadrātiem.
# 4. uzdevums (1MPR02_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas izveido zemāk redzamo attēlu, izmantojot rekursiju.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


import tkinter


def rinka_linija(x, y, r):
    # Izveido riņķa līniju kurai centrs ir (x;y) un rādiuss ir r
    # x - x koordināta riņķa līnijas centram
    # y - y koordināta riņķa līnijas centram
    # r - riņķa līnijas rādiuss
    kanva.create_oval(x - r, y - r, x + r, y + r)


def kvadrats(x, y, r):
    # Izveido kvadrātu pēc dota centra koordinātam (x;y) un pēc r (puse no kvadrātas malas)
    # x - x koordināta kvadrātas centram
    # y - y koordināta kvadrātas centram
    # r - puse no kvadrātas malas (lai uzzimētu kvadrātu)
    kanva.create_rectangle(x - r, y - r, x + r, y + r)


def rekursija_1(x, y, r):
    # Uzzime kvadrātu un četras riņķa līnijas blakus pa visam pusem
    # x - x koordināta centram
    # y - y koordināta centram
    # r - rādiuss riņķa līnijai vai puse no kvadrātas malas
    kvadrats(x, y, r)
    if r > 5:
        rekursija_2(x + 3 * r, y, r / 3)
        rekursija_2(x - 3 * r, y, r / 3)
        rekursija_2(x, y + 3 * r, r / 3)
        rekursija_2(x, y - 3 * r, r / 3)


def rekursija_2(x, y, r):
    # Uzzime riņķa līniju un četrus kvadrātus blakus pa visam pusem
    # x - x koordināta centram
    # y - y koordināta centram
    # r - rādiuss riņķa līnijai vai puse no kvadrātas malas
    rinka_linija(x, y, r)
    if r > 5:
        rekursija_1(x + 3 * r, y, r / 3)
        rekursija_1(x - 3 * r, y, r / 3)
        rekursija_1(x, y + 3 * r, r / 3)
        rekursija_1(x, y - 3 * r, r / 3)


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


logs = tkinter.Tk()
kanva = tkinter.Canvas(logs, bg="#EDEDED", height=1200, width=1200)
kanva.pack()
logs.title("Rekursija")

rekursija_2(600, 500, 100)

logs.mainloop()
