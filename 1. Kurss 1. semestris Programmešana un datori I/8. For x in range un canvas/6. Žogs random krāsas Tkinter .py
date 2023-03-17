# Programmas nosaukums: 4. uzd MPR8 PU
# 4. uzdevums MPR8 PU
# Uzdevuma formulējums: Uzzīmēt žogu ar latiņām katru savā krāsā.
# Versija 1.0

import tkinter
from tkinter import ttk

from random import randrange


def zogs():
    
    for x in range (50, 500, 100):
        global x1,y1,x2,y2
        color_c='#%02x%02x%02x' % (randrange(256), randrange(256), randrange(256)) # random rgb colour => HEX

        kanva.create_line(x, 30, x, 400, width=15, fill=color_c) # fill ar random color (vertikalas latinas)
        
    for y in range (100, 400, 230):
    
        kanva.create_line(0, y, 700, y, width=15, fill="black") # melnas horizontālas latiņas 
        
    
def notirit():
    kanva.delete("all") # notirisanai
    
logs = tkinter.Tk()
logs.geometry("700x700")

kanva = tkinter.Canvas(logs, bg="white", height=500, width=500)
kanva.place(x=100, y=10)
poga1= ttk.Button(logs, text="Žogs", command=zogs)
poga1.place(x=10,y=10)
poga2 = ttk.Button(logs, text="Notīrīt", command=notirit)
poga2.place(x=10, y=50)

logs.mainloop()