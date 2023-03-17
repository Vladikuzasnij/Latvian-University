# Programmas nosaukums: Rekursija. Daudz riņķa līnijas.
# Papilduzdevums 2. (1MPR02_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas izveido zemāk redzamo attēlu, izmantojot rekursiju.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


import tkinter
import math


logs = tkinter.Tk()
logs.geometry("1000x1000")
W = 1000
H = 1000
canva = tkinter.Canvas(logs, width=W, height=H)
canva.configure(background='white')
canva.pack()

CENTRS_X = W // 2
CENTRS_Y = H // 2


def get_new_pos(x, y, lenkis, attalums):
    # Saņem x un y koordinātas, leņķi un attālumu un atgriež jauno pozīciju pēc dotā attāluma pārvietošanas dotajā leņķī
    # x - jaunais x
    # y - jaunais y
    # lenkis - leņķis grādos
    # attalums - attālums
    return x + attalums * math.cos(math.radians(lenkis)), y + attalums * math.sin(math.radians(lenkis))


def draw_circle(center_x, center_y, r):
    # Pēc dota centras koordinātas (center_x, center_y) un rādiusa (r) uzzīmē riņķa līniju.
    # center_x - riņķa līnijas centrs pēc x koordinātas
    # center_y - riņķa līnijas centrs pēc y koordinātas
    # r - riņķa līnijas rādiuss
    x1 = center_x - r
    x2 = center_x + r
    y1 = center_y - r
    y2 = center_y + r
    #print(x1, x2, y1, y2)
    canva.create_oval(x1, y1, x2, y2)


def recursion(center_x, center_y, r, rekursijas_skaits):
    # Tas saņem pašreizējās iterācijas centra koordinātas, rādiusu un dziļuma līmeni (rekursijas skaits).
    # Katrā dziļuma līmenī (rekursijas skaitam) tiek uzzīmēta riņķa līnijas pie dotajām centra koordinātām
    # un pēc tam funkcija tiek rekursīvi izsaukta ar sešām jaunām centra koordinātām,
    # kuras aprēķina, izmantojot funkciju get_new_pos.
    # center_x - riņķa līnijas centrs pēc x koordinātas
    # center_y - riņķa līnijas centrs pēc y koordinātas
    # r - riņķa līnijas rādiuss
    # rekursijas_skaits - rekursījas dziļums (cik reizes rekursija tiek īstenota)

    draw_circle(center_x, center_y, r)

    if rekursijas_skaits == 0:
        return
    attalums = r * 2 / 3
    jauns_radiuss = r / 3 # apzīmē mazāko apļu rādiusu, kas rekursīvi apvilkti ap lielākiem apļiem.
    lenkis = 30 # 30 grādi

    for t in range(6): # t netiek izmantota
        new_x, new_y = get_new_pos(center_x, center_y, lenkis, attalums)
        recursion(new_x, new_y, jauns_radiuss, rekursijas_skaits - 1)
        lenkis = lenkis + 60 # Katras jaunās centra koordinātas leņķis tiek nobīdīts par 60 grādiem no iepriekšējās, jo ap pašreizējo apli ir sešas riņķa līnijas

    recursion(center_x, center_y, jauns_radiuss, rekursijas_skaits - 1)


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


recursion(CENTRS_X, CENTRS_Y, 400, 2)

logs.mainloop()
