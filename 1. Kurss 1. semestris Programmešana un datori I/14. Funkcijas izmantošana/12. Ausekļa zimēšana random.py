# Importējam Tkinter un random bibliotēkas
import random
import tkinter
from tkinter import ttk
from random import randrange

# Definējam procedūru, kas uzzīmē ausekli norādītajā vietā, krāsā un izmērā
def draw_auseklis(x, y, r, color):
    #Uz ekrāna uzzīmējam ausekli
    kanva.create_polygon(x,y-2*r,   x+r,y-3*r,   x+r,y-r,   x+3*r,y-r,  x+2*r,y,  x+3*r,y+r,   x+r,y+r,  x+r,y+3*r,  x,y+2*r,  x-r,y+3*r,   x-r,y+r,   x-3*r,y+r,   x-2*r,y,   x-3*r, y-r,   x-r,y-r, x-r,y-3*r, fill=color)

def paradit():
    auseklu_skaits = int(random.randint(1,100)) # Iegūstam nejaušu skaitli no 1 līdz 100, lai noteiktu ausekļu skaitu

    # Iegūstam nejaušas krāsas un izmērus ausekļiem
    for i in range(auseklu_skaits):
        x = int(random.randint(1,900)) # centrs pēc x
        y = int(random.randint(1,900)) # centrs pēc y
        r = int(random.randint(1,30)) # izmers
        color='#%02x%02x%02x' % (randrange(256), randrange(256), randrange(256)) #nejaušas krāsa
        draw_auseklis(x,y, r, color)

def notirit():
    kanva.delete("all") # notirisanai

logs = tkinter.Tk()
logs.geometry("1000x1000")
kanva = tkinter.Canvas(logs, bg="white", height=900, width=900)
kanva.place(x=100, y=10)
poga1= ttk.Button(logs, text="Parādīt", command=paradit)
poga1.place(x=10,y=10)
poga2 = ttk.Button(logs, text="Notīrīt", command=notirit)
poga2.place(x=10, y=50)
logs.mainloop()