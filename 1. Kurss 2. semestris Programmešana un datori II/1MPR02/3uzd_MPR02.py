# Programmas nosaukums: Rekursija. Riņķa līnijas.
# 3. uzdevums (1MPR02_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas izveido zemāk redzamo attēlu, izmantojot rekursiju.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


import tkinter
from tkinter import ttk


def create_circle(x, y, r):
    # Uzzīme riņķa līniju
    # r - riņķa līnijas rādiuss
    # x - x koordināta riņķa līnijas centram
    # y - y koordināta riņķa līnijas centram
    kanva.create_oval(x - r, y - r, x + r, y + r, outline="black", width=3)


def draw_circles(x, y, r): # r - rādiuss
    # Uzzīme riņķa līnijas rekursīvi uz labo pusi
    # r - riņķa līnijas rādiuss
    # x - x koordināta riņķa līnijas centram
    # y - y koordināta riņķa līnijas centram
    if r >= 2:
        create_circle(x, y, r)
        draw_circles(x + r, y, r // 2)


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


logs = tkinter.Tk()
logs.geometry("1200x900")
logs.title("Rekursija")

kanva = tkinter.Canvas(logs, bg="white", height=700, width=1000)
kanva.place(x=100, y=90)

draw_circles(350, 350, 300)

logs.mainloop()
