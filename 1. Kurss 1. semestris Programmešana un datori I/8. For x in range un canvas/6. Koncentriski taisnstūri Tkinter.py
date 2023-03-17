# Programmas nosaukums: 8. uzd MPR8
# 8. uzdevums MPR8
# Uzdevuma formulējums: Uzzīmēt koncentriskus taisnstūrus
# Versija 1.0

import tkinter
from tkinter import ttk

x1 = 350
y1 = 300

x2 = 550
y2 = 400

def paradit():

    x1 = 400
    y1 = 400
    
    x2 = 450
    y2 = 420
    
    for a in range (0, 390, 10):   
        kanva.create_rectangle(x1-a, y1 - a, x2 + a, y2 + a)

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