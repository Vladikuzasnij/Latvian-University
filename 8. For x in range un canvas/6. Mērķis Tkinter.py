# Programmas nosaukums: 9. uzd MPR8 PU3
# 9. uzdevums MPR8 PU3
# Uzdevuma formulējums: Uzzīmēt mērķi.
# Versija 1.0


import tkinter
from tkinter import ttk
from random import randrange


def paradit():
    
    for a in range (0, 400, 50):
        
        x1 = 50
        y1 = 50
        
        x2 = 700
        y2 = 700       
        
        
        color_c='#%02x%02x%02x' % (randrange(256), randrange(256), randrange(256))
        
        kanva.create_oval(x1+a, y1 + a, x2 - a, y2 - a, fill=color_c, outline="")
    

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