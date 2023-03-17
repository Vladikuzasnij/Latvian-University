# Programmas nosaukums: 4. uzd MPR8
# 4. uzdevums MPR8
# Uzdevuma formulējums: Uzzīmēt žogu visu vienā krāsā.
# Versija 1.0

import tkinter
from tkinter import ttk

def zogs():

    for x in range (50, 500, 100):   
        kanva.create_line(x, 30, x, 400, width=7, fill="blue")
    
    for y in range (100, 400, 230):   
        kanva.create_line(0, y, 700, y, width=7, fill="blue")    
    
def notirit():
    kanva.delete("all") # notirisanai
    
logs = tkinter.Tk()
logs.geometry("700x600")

kanva = tkinter.Canvas(logs, bg="white", height=500, width=500)
kanva.place(x=100, y=10)
poga1= ttk.Button(logs, text="Parādīt", command=zogs)
poga1.place(x=10,y=10)
poga2 = ttk.Button(logs, text="Notīrīt", command=notirit)
poga2.place(x=10, y=50)

logs.mainloop()